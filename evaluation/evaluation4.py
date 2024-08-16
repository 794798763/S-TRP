#实验不同情况下关系损失RLOSS
import matplotlib.pyplot as  plt
import numpy as np
import random
import time

total_textwidth=5.8

def test1(lmin,lmax,tao,outN,offset):

    #测试不同tao时，关系的损失
    #outN是要输出的采样的点
    #offset是为了方便画图 使点不重叠 所以做的x轴偏移
    N=200
    X=[]
    Y=[]
    F=10
    d=2

    #先判断N够不够用，不够用不生成
    #d是delt
    if (d*F+1)*tao>=N:
        return [],[]

    for l in range(lmin,lmax+1):
        #要进行outN次实验
        for ti in range(outN):
            count = [0 for _ in range(N)]
            # 开始分发被追踪的交易，每个交易只分布在一个高度
            for i in range(int(l)):
                for j in random.sample(list(range(N)), d * F + 1):
                    count[j] = count[j] + 1
            # 查看是否有节点能还原出来
            re = 0
            for i in count:
                if i == l:
                    re = re + 1
            X.append(l+offset)
            Y.append(1-re/(d*F+1))
    return X,Y

def draw1():
    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.grid()
    lmin=1
    lmax=8

    X,Y=test1(lmin,lmax,2,10,-0.15)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='g', s=10)

    X, Y = test1(lmin, lmax, 8, 10, 0)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='b', s=10)

    X, Y = test1(lmin, lmax, 16, 10, 0.15)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='y', s=10)

    plt.subplots_adjust(left=0.15)
    plt.show()

def test2(lmin,lmax,d,outN,offset):

    #测试不同tao时，关系的损失
    #outN是要输出的采样的点
    #offset是为了方便画图 使点不重叠 所以做的x轴偏移
    N=200
    X=[]
    Y=[]
    F=10
    tao=4

    #先判断N够不够用，不够用不生成
    #d是delt
    if (d*F+1)*tao>=N:
        return [],[]

    for l in range(lmin,lmax+1):
        #要进行outN次实验
        for ti in range(outN):
            count = [0 for _ in range(N)]
            # 开始分发被追踪的交易，每个交易只分布在一个高度
            for i in range(int(l)):
                for j in random.sample(list(range(N)), d * F + 1):
                    count[j] = count[j] + 1
            # 查看是否有节点能还原出来
            re = 0
            for i in count:
                if i == l:
                    re = re + 1
            X.append(l+offset)
            Y.append(1-re/(d*F+1))
    return X,Y

def draw2():
    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.grid()
    lmin=1
    lmax=8

    X,Y=test2(lmin,lmax,2,20,-0.15)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='g', s=10)

    X, Y = test2(lmin, lmax, 3, 20, 0)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='b', s=10)

    plt.subplots_adjust(left=0.15)
    plt.show()


def test3(lmin,lmax,F,outN,offset):

    #测试不同tao时，关系的损失
    #outN是要输出的采样的点
    #offset是为了方便画图 使点不重叠 所以做的x轴偏移
    N=200
    X=[]
    Y=[]
    d=2
    tao=2

    #先判断N够不够用，不够用不生成
    #d是delt
    if (d*F+1)*tao>=N:
        return [],[]

    for l in range(lmin,lmax+1):
        #要进行outN次实验
        for ti in range(outN):
            count = [0 for _ in range(N)]
            # 开始分发被追踪的交易，每个交易只分布在一个高度
            for i in range(int(l)):
                for j in random.sample(list(range(N)), d * F + 1):
                    count[j] = count[j] + 1
            # 查看是否有节点能还原出来
            re = 0
            for i in count:
                if i == l:
                    re = re + 1
            X.append(l+offset)
            Y.append(1-re/(d*F+1))
    return X,Y

def draw3():
    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.grid()
    lmin=1
    lmax=8

    X,Y=test3(lmin,lmax,3,50,-0.15)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='g', s=10)

    X,Y=test3(lmin,lmax,10,50,0)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='b', s=10)

    X, Y = test3(lmin, lmax, 20, 50, 0.15)
    X = np.array(X)
    Y = np.array(Y)
    axe.scatter(X, Y, c='y', s=10)

    plt.subplots_adjust(left=0.15)
    plt.show()

for i in range(10):
    draw1()