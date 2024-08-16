import matplotlib.pyplot as  plt
import numpy as np
import math


#安全性分析章节的实验图

total_textwidth=5.8
x_labels = ['sdf', 'sdf', 'sdert', 'sdf', 'hg', 'ghjf', 'sdf', 'asdfghj']

def draw1():
    x_points=np.array([0,100])
    y_points=np.array([0,100])

    plt.figure(figsize=(1.9, 2), dpi=300)
    plt.subplots_adjust(left=0.2)
    plt.plot(x_points,y_points)
    plt.show()



def draw2():
    fig=plt.figure(figsize=(1.9, 4), dpi=300)

    x_points=np.array([99,105])
    y_points=np.array([99,200])
    plot=fig.add_subplot(111)
    plot.plot(x_points,y_points)
    plt.show()

def draw3():
    X=np.linspace(-4,4,400)
    Y=np.linspace(-4,4,400)
    X,Y=np.meshgrid(X,Y)
    Z=np.cos(np.sqrt(X**2+Y**2))

    plt.figure(figsize=(total_textwidth/2-0.1,2),dpi=300)

    # plt.subplots_adjust(left=2)

    axes=plt.axes(projection="3d")
    surf=axes.plot_surface(X,Y,Z,cmap=plt.get_cmap("plasma"))


    plt.colorbar(surf)
    plt.show()

def draw4():
    X=np.linspace(1,10,100) #l 关系长度

    Y=np.linspace(3,10,100) # tao 扩展比

    #长度取整
    for i in range(len(X)):
        X[i]=int(X[i])
    for i in range(len(Y)):
        #取整数
        Y[i]=10/math.ceil(10/Y[i])
    X,Y=np.meshgrid(X,Y)
    Z=1-(1/Y)**X

    fig=plt.figure(figsize=(total_textwidth/2-0.1 , 3), dpi=300)
    axes=plt.axes(projection="3d")
    surf=axes.plot_surface(X,Y,Z,cmap=plt.get_cmap("plasma"))
    # plt.colorbar(surf)

    #单独画colorbar
    fig.colorbar(surf,orientation='vertical',pad=0.5)

    plt.show()


def draw5():
    X=np.linspace(1,10,100) #l 关系长度
    #长度取整
    for i in range(len(X)):
        X[i]=int(X[i])

    Y=np.linspace(3,10,100) # tao 扩展比
    Z=[]
    for i in X:
        templist=[]
        for j in Y:
            temp=P_rloss_L(i,j)
            templist.append(temp)
        Z.append(templist)
    Z=np.array(Z)
    X,Y=np.meshgrid(X,Y)
    fig=plt.figure(figsize=(total_textwidth/2-0.1 , 3), dpi=300)
    axes=plt.axes(projection="3d")
    surf=axes.plot_surface(X,Y,Z,cmap=plt.get_cmap("plasma"))
    plt.show()





def P_rloss_L(l,tao):
    N=10
    D=math.ceil(N/tao)
    l=int(l)
    re=0
    re2=1
    for k in range(1,D+1):
        re=re+f(l,k,N,D)
    # print(re)
    for i in range(l):
        re2=re2*C(N,D)
    # print(re2)
    return 1-re/re2

def f(l,k,N,D):
    #超参D为 德尔塔*F+1
    #超参N为节点总数

    re=0
    if l==1:
        return C(N,D)
    if l==2:
        # print(C(N,D))
        # print(C(D,k))
        # print(C(N-D,D-k))
        return C(N,D)*C(D,k)*C(N-D,D-k)
    for i in range(k,D+1):
        re=re+f(l-1,i,N,D)*C(i,k)*C(N-i,D-k)
        # print(re)
    return re


def C(n,m):
    re1=1
    re2=1
    re3=1
    if n==m:
        return 1
    if m==0:
        return 1
    if n==0:
        return 1
    for i in range(1,n+1):
        re1=re1*i
    for i in range(1,m+1):
        re2=re2*i
    for i in range(1,n-m+1):
        re3=re3*i
    return re1/(re2*re3)

print(P_rloss_L(3,3))
