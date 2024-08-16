#性能实验图绘图
import matplotlib.pyplot as  plt
import numpy as np
import math

total_textwidth=5.8
styles = ['c:s', 'y:8', 'r:^', 'r:v', 'g:D', 'm:X', 'b:p', ':>']

def draw1():
    #节点数量N对交易延迟的影响
    plt.rc('legend', fontsize=10)

    X=[8,12,16,20]
    Y_ours=[520,525,510,525]
    Y_sharper=[390,500,605,800]
    Y_Meepo=[200,250,300,320]

    X=np.array(X)
    Y_ours=np.array(Y_ours)
    Y_sharper=np.array(Y_sharper)
    Y_Meepo=np.array(Y_Meepo)

    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.plot(X,Y_ours,linestyle='-',color='b',marker='*',label='ours-')
    axe.plot(X,Y_sharper,linestyle='--',color='g',marker='v',label='sharper')
    axe.plot(X,Y_Meepo,linestyle='--',color='y',marker='s',label='Meepo')

    # # 设置图片的x,y轴的限制，和对应的标签
    # plt.xlim([0, 300])
    # plt.ylim([60, 78])
    # plt.xlabel("GFLOPs/Video")
    # plt.ylabel("mAP(%)")

    # 设置图片的方格线和图例
    plt.grid()
    plt.legend(loc='upper left', framealpha=0.7)
    plt.tight_layout()
    plt.show()


def draw2():
    #节点数量N对系统吞吐量的影响
    plt.rc('legend', fontsize=10)

    X=[4,8,16,20]
    Y_ours=[15,24,26,32]
    Y_PBFT=[3,2.5,2,1]
    Y_Meepo=[10,14,16,18]

    X=np.array(X)
    Y_ours=np.array(Y_ours)
    Y_PBFT=np.array(Y_PBFT)
    Y_Meepo=np.array(Y_Meepo)

    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.plot(X,Y_ours,linestyle='-',color='b',marker='*',label='ours-')
    axe.plot(X,Y_PBFT,linestyle='--',color='g',marker='v',label='PBFT')
    axe.plot(X,Y_Meepo,linestyle='--',color='y',marker='s',label='Meepo')

    # # 设置图片的x,y轴的限制，和对应的标签
    # plt.xlim([0, 300])
    # plt.ylim([60, 78])
    # plt.xlabel("GFLOPs/Video")
    # plt.ylabel("mAP(%)")

    # 设置图片的方格线和图例
    plt.grid()
    plt.legend(loc='upper left', framealpha=0.7)
    plt.tight_layout()
    plt.show()

def draw3():
    #不同冲突概率下吞吐与延迟关系
    plt.rc('legend', fontsize=10)

    X_20=[10,20,30,33]
    Y_20=[600,850,2100,3100]

    X_80=[10,20,30,31,32]
    Y_80=[600,1000,2800,3600,5600]

    X_20=np.array(X_20)
    X_80=np.array(X_80)
    Y_20=np.array(Y_20)
    Y_80=np.array(Y_80)

    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.plot(X_20,Y_20,linestyle='-',color='b',marker='*',label='20%')
    axe.plot(X_80,Y_80,linestyle='--',color='g',marker='v',label='80%')

    # # 设置图片的x,y轴的限制，和对应的标签
    # plt.xlim([0, 300])
    # plt.ylim([60, 78])
    # plt.xlabel("GFLOPs/Video")
    # plt.ylabel("mAP(%)")

    # 设置图片的方格线和图例
    plt.grid()
    plt.legend(loc='upper left', framealpha=0.7)
    plt.tight_layout()
    plt.show()

def draw4():
    #不同arrival rate下的吞吐量 (32个shard)
    #暂时废弃
    plt.rc('legend', fontsize=10)

    X=[10,20,50,80]

    Y_ours=[10,20,45,64]
    Y_brokerchain=[10,17,26,26]

    X=np.array(X)
    Y_ours=np.array(Y_ours)
    Y_brokerchain=np.array(Y_brokerchain)

    fig,axe=plt.subplots(figsize=(total_textwidth / 2 - 0.1, 2), dpi=300)
    axe.plot(X,Y_ours,linestyle='-',color='b',marker='*',label='ours-')
    axe.plot(X,Y_brokerchain,linestyle='--',color='g',marker='v',label='brokerchain')

    # # 设置图片的x,y轴的限制，和对应的标签
    # plt.xlim([0, 300])
    # plt.ylim([60, 78])
    # plt.xlabel("GFLOPs/Video")
    # plt.ylabel("mAP(%)")

    # 设置图片的方格线和图例
    plt.grid()
    plt.legend(loc='upper left', framealpha=0.7)
    plt.tight_layout()
    plt.show()
draw1()
draw2()
draw3()