匿踪对比可追溯：可追溯是指发起者能够向任何人证明 该过程（一系列交易）确实发生了且被验证通过了
方法是要给client的交易生成merkleproof，证明他的交易确实没问题。client只要出示一系列交易的proof 就能证明该过程


# Cryptopia失窃：
## 源地址 
0xd4e79226f1e5a7a28abb58f4704e53cd364e8d11
## 目标地址
yobit.net 地址 0xf5bec430576ff1b82e44ddb5a1c93f6f9d0884f3

EtherDelta 地址 0x338fdf0d792f7708d97383eb476e9418b3c16ff1

EtherDelta 地址 0x4aea7cf559f67cedcad07e12ae6bc00f07e8cf65

EtherDelta 地址 0x8d12a197cb00d4747a1fe03395095ce2a5cc6819

EtherDelta 地址 0xce53a179047ebed80261689367c093c90a94cc08

OKEx 地址 0x776bb566dc299c9e722773d2a04b401e831a6dc8
## 追踪结果

id	hash	from	to	value	timeStamp	blockNumber	symbol	contractAddress
0x0a83229459dd79251aea471b39e9def78bef0d96bf6781f200017a68edc6a82d_None_native_	0x0a83229459dd79251aea471b39e9def78bef0d96bf6781f200017a68edc6a82d	0xd4e79226f1e5a7a28abb58f4704e53cd364e8d11	0x845f93f489b524f19864db6e0ab581c532b58d36	1E+18	1559038504	7847428	native_	

### tracer：

 'finish_time': datetime.datetime(2023, 9, 12, 8, 14, 17, 114070),

 'request_depth_max': 378,

 'start_time': datetime.datetime(2023, 9, 12, 8, 10, 55, 886601)}

node number 119357

##对比实验

1. 深度优先遍历

直接在爬虫数据上进行深度优先遍历，会获得大量的点和边
   
2. 时序监听

分片结果会影响时序监听的效果
删掉了值不足1以太币的交易
在爬虫数据上进行时序清洗（清洗的过程本质上就是重放交易，将可疑地址逐个标记，然后追踪这些地址的相关交易），清洗后的交易都是符合先后顺序的。然后进行深度优先遍历。

3. tracer 

在时序监听的基础上，把相同起点终点的交易都合并了。
tracer需要画展示图。画的时候可以删掉深度比较浅的边和点。
然后只保留（展示）部分点（边）。


# Cryptopia失窃：