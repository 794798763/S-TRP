package params

var (
	Block_Interval      = 5000   // generate new block interval
	MaxBlockSize_global = 2000   // the block contains the maximum number of transactions
	InjectSpeed         = 2000   // the transaction inject speed
	TotalDataSize       = 100000 // the total number of txs
	BrokerNum           = 10
	NodesInShard        = 4
	ShardNum            = 4
	DataWrite_path      = "./result/"       // measurement data result output path
	LogWrite_path       = "./log"           // log output path
	SupervisorAddr      = "127.0.0.1:18800" //supervisor ip address
	//数据引用地址@article{Zheng2020,
	//author = {Zheng, Peilin and Zheng, Zibin and Wu, Jiajing and Dai, Hong-Ning},
	//doi = {10.1109/OJCS.2020.2990458},
	//journal = {IEEE Open J. Comput. Soc.},
	//pages = {95--106},
	//publisher = {IEEE},
	//title = {{XBlock-ETH: Extracting and exploring blockchain data from Ethereum}},
	//volume = {1},
	//month = {May},
	//year = {2020}
	//}
	FileInput = `../2000000to2999999_BlockTransaction.csv` //the raw BlockTransaction data path
)
