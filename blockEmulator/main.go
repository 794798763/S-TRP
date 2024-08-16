package main

import (
	"blockEmulator/build"

	"github.com/spf13/pflag"
)

var (
	shardNum int
	nodeNum  int
	shardID  int
	nodeID   int
	modID    int
	isClient bool
	isGen    bool
)

func main() {
	pflag.IntVarP(&shardNum, "shardNum", "S", 2, "indicate that how many shards are deployed")
	pflag.IntVarP(&nodeNum, "nodeNum", "N", 4, "indicate how many nodes of each shard are deployed")
	pflag.IntVarP(&shardID, "shardID", "s", 0, "id of the shard to which this node belongs, for example, 0")
	pflag.IntVarP(&nodeID, "nodeID", "n", 0, "id of this node, for example, 0")
	//自己写的新方法就添加一个新mod
	pflag.IntVarP(&modID, "modID", "m", 3, "choice Committee Method,for example, 0, [CLPA_Broker,CLPA,Broker,Relay] ")
	pflag.BoolVarP(&isClient, "client", "c", false, "whether this node is a client")
	//是否生成自启动项目的脚本
	pflag.BoolVarP(&isGen, "gen", "g", false, "generation bat")
	pflag.Parse()

	if isGen {
		build.GenerateBatFile(nodeNum, shardNum, modID)
		return
	}

	if isClient {
		//client就是Supervisor，特权的能够看到整个网络的节点
		build.BuildSupervisor(uint64(nodeNum), uint64(shardNum), uint64(modID))
	} else {
		build.BuildNewPbftNode(uint64(nodeID), uint64(nodeNum), uint64(shardID), uint64(shardNum), uint64(modID))
	}
}
