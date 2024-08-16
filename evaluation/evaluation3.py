#实验不同情况下节点交易损失NLOSS
import matplotlib.pyplot as  plt
import numpy as np
import random
import time

total_textwidth=5.8

def test1(N,d,outN):

    #测试不同德尔塔时，节点的损失
    #outN是要输出的采样的点
    X=[]
    Y=[]
    count=[0 for _ in range(N)]
    F=10
    tao=4
    #是十万笔交易中追踪txs/blockSize笔交易
    txs=100000
    #区块大小是blockSize
    blockSize=100

    #先判断N够不够用，不够用不生成点
    #d是delt
    if (d*F+1)*tao>=N:
        return X,Y
    #开始分发被追踪的交易，每个交易只分布在一个高度
    for i in range(int(txs/blockSize)):
        for j in random.sample(list(range(N)), d*F+1):
            count[j]=count[j]+1
    #输出结果,先找到被采样的outN个点
    for i in range(outN):
        ran=random.randint(0,N-1)
        X.append(N)
        Y.append(1-count[ran]/(txs/blockSize))
    return X,Y

def draw1():
    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.grid()
    #x轴上一共x_sample个采样点
    for x_sample in range(int(100/10),int(800/10)+1):
        X,Y=test1(x_sample*10,2,10)
        X=np.array(X)
        Y=np.array(Y)
        axe.scatter(X,Y,c='g',s=3)

        X,Y=test1(x_sample*10,3,10)
        X=np.array(X)
        Y=np.array(Y)
        axe.scatter(X,Y,c='b',s=3)
    plt.show()


def test2(N,tao,outN):

    #测试不同tao时，节点的损失
    #outN是要输出的采样的点
    X=[]
    Y=[]
    count=[0 for _ in range(N)]
    F=10
    d=2
    #是十万笔交易中追踪txs/blockSize笔交易
    txs=100000
    #区块大小是blockSize
    blockSize=100

    #先判断N够不够用，不够用不生成点
    #d是delt
    if (d*F+1)*tao>=N:
        return X,Y
    #开始分发被追踪的交易，每个交易只分布在一个高度
    for i in range(int(txs/blockSize)):
        for j in random.sample(list(range(N)), d*F+1):
            count[j]=count[j]+1
    #输出结果,先找到被采样的outN个点
    for i in range(outN):
        ran=random.randint(0,N-1)
        X.append(N)
        Y.append(1-count[ran]/(txs/blockSize))
    return X,Y


def draw2():
    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.grid()
    #x轴上一共x_sample个采样点
    for x_sample in range(int(100/10),int(800/10)+1):
        X,Y=test2(x_sample*10,2,10)
        X=np.array(X)
        Y=np.array(Y)
        axe.scatter(X,Y,c='g',s=3)

        X,Y=test2(x_sample*10,16,10)
        X=np.array(X)
        Y=np.array(Y)
        axe.scatter(X,Y,c='b',s=3)

        X, Y = test2(x_sample * 10, 32, 10)
        X = np.array(X)
        Y = np.array(Y)
        axe.scatter(X, Y, c='y', s=3)

    plt.subplots_adjust(left=0.15)
    plt.show()


def test3(N,F,outN):

    #测试不同F时，节点的损失
    #outN是要输出的采样的点
    X=[]
    Y=[]
    count=[0 for _ in range(N)]
    tao=4
    d=2
    #是十万笔交易中追踪txs/blockSize笔交易
    txs=100000
    #区块大小是blockSize
    blockSize=100

    #先判断N够不够用，不够用不生成点
    #d是delt
    if (d*F+1)*tao>=N:
        return X,Y
    #开始分发被追踪的交易，每个交易只分布在一个高度
    for i in range(int(txs/blockSize)):
        for j in random.sample(list(range(N)), d*F+1):
            count[j]=count[j]+1
    #输出结果,先找到被采样的outN个点
    for i in range(outN):
        ran=random.randint(0,N-1)
        X.append(N)
        Y.append(1-count[ran]/(txs/blockSize))
    return X,Y

def draw3():
    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.grid()
    #x轴上一共x_sample个采样点
    for x_sample in range(int(100/10),int(800/10)+1):
        X,Y=test3(x_sample*10,3,10)
        X=np.array(X)
        Y=np.array(Y)
        axe.scatter(X,Y,c='g',s=3)

        X,Y=test3(x_sample*10,10,10)
        X=np.array(X)
        Y=np.array(Y)
        axe.scatter(X,Y,c='b',s=3)

        X, Y = test3(x_sample * 10, 20, 10)
        X = np.array(X)
        Y = np.array(Y)
        axe.scatter(X, Y, c='y', s=3)

    plt.subplots_adjust(left=0.15)
    plt.show()



draw1()
draw2()
draw3()