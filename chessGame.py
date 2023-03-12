# import random
EVENT_WIN=1
EVENT_LOSE=2
EVENT_RESTART=3
EVENT_REGRET=4
EVENT_NORMAL=5
CHESS_NULL=0
CHESS_WHITE=2
CHESS_BLACK=1
ONE_BLACK=35
TWO_BLACK=800
THREE_BLACK=15000
FOUR_BLACK=800000
FIVE_BLACK=float('inf')
ONE_WHITE=-35
TWO_WHITE=-800
THREE_WHITE=-15000
FOUR_WHITE=-800000
FIVE_WHITE=-float('inf')
NOCHESS=7
DEPTH=2 #  搜索深度
alpha=-float('inf')
beta=float('inf')
class StornPoint():
    def __init__(self, x, y, value):
        '''
        :param x: 代表x轴坐标
        :param y: 代表y轴坐标
        :param value: 当前坐标点的棋子：0:没有棋子 1:黑子 2:白子
        '''
        self.x = x  # 初始化成员变量
        self.y = y
        self.value = value

step=StornPoint(0,0,0)
'''
------------------------------------------------------
函数名：evaluatePoint
函数参数：initChessList : 棋盘数组
        i : 要评估的点的横坐标
        j : 要评估的点的纵坐标
功能： 计算一个点的评估值，评估值就是以那个点为头的五元组
返回值： 返回该点的评估值
------------------------------------------------------
'''
def evaluatePoint(initChessList,i,j):
    sum=0
    flags=[0,0,0,0]
    count_B=0
    count_W=0
    for m in range(5):
        if initChessList[i+m][j].value==CHESS_NULL:
            pass
        elif initChessList[i+m][j].value==CHESS_BLACK and count_W==0:
            count_B+=1
        elif initChessList[i+m][j].value==CHESS_WHITE and count_B==0:
            count_W+=1
        elif initChessList[i+m][j].value==CHESS_WHITE and count_B!=0:
            flags[0]=1
            break
        elif initChessList[i+m][j].value==CHESS_BLACK and count_W!=0:
            flags[0]=1
            break
    if flags[0]==0:
        if count_B==1:
            sum+=ONE_BLACK
        elif count_B==2:
            sum+=TWO_BLACK
        elif count_B==3:
            sum+=THREE_BLACK
        elif count_B==4:
            sum+=FOUR_BLACK
        elif count_B==5:
            sum=FIVE_BLACK
        elif count_W==1:
            sum+=ONE_WHITE
        elif count_W==2:
            sum+=TWO_WHITE
        elif count_W==3:
            sum+=THREE_WHITE
        elif count_W==4:
            sum+=FOUR_WHITE
        elif count_W==5:
            sum=FIVE_WHITE
        elif count_W==0 and count_B==0:
            sum+=NOCHESS

    if j<=10:
        count_B=0
        count_W=0
        for m in range(5):
            if initChessList[i][j+m].value==CHESS_NULL:
                pass
            elif initChessList[i][j+m].value==CHESS_BLACK and count_W==0:
                count_B+=1
            elif initChessList[i][j+m].value==CHESS_WHITE and count_B==0:
                count_W+=1
            elif initChessList[i][j+m].value==CHESS_WHITE and count_B!=0:
                flags[1]=1
                break
            elif initChessList[i][j+m].value==CHESS_BLACK and count_W!=0:
                flags[1]=1
                break
        if flags[1]==0:
            if count_B == 1:
                sum += ONE_BLACK
            elif count_B == 2:
                sum += TWO_BLACK
            elif count_B == 3:
                sum += THREE_BLACK
            elif count_B == 4:
                sum += FOUR_BLACK
            elif count_B == 5:
                sum = FIVE_BLACK
            elif count_W == 1:
                sum += ONE_WHITE
            elif count_W == 2:
                sum += TWO_WHITE
            elif count_W == 3:
                sum += THREE_WHITE
            elif count_W == 4:
                sum += FOUR_WHITE
            elif count_W == 5:
                sum = FIVE_WHITE
            elif count_W == 0 and count_B == 0:
                sum += NOCHESS

        count_B = 0
        count_W = 0
        for m in range(5):
            if initChessList[i+ m][j + m].value == CHESS_NULL:
                pass
            elif initChessList[i+ m][j + m].value == CHESS_BLACK and count_W == 0:
                count_B += 1
            elif initChessList[i+ m][j + m].value == CHESS_WHITE and count_B == 0:
                count_W += 1
            elif initChessList[i+ m][j + m].value == CHESS_WHITE and count_B != 0:
                flags[2] = 1
                break
            elif initChessList[i+ m][j + m].value == CHESS_BLACK and count_W != 0:
                flags[2] = 1
                break
        if flags[2] == 0:
            if count_B == 1:
                sum += ONE_BLACK
            elif count_B == 2:
                sum += TWO_BLACK
            elif count_B == 3:
                sum += THREE_BLACK
            elif count_B == 4:
                sum += FOUR_BLACK
            elif count_B == 5:
                sum = FIVE_BLACK
            elif count_W == 1:
                sum += ONE_WHITE
            elif count_W == 2:
                sum += TWO_WHITE
            elif count_W == 3:
                sum += THREE_WHITE
            elif count_W == 4:
                sum += FOUR_WHITE
            elif count_W == 5:
                sum = FIVE_WHITE
            elif count_W == 0 and count_B == 0:
                sum += NOCHESS

    if j>=4:
        count_B = 0
        count_W = 0
        for m in range(5):
            if initChessList[i + m][j - m].value == CHESS_NULL:
                pass
            elif initChessList[i + m][j - m].value == CHESS_BLACK and count_W == 0:
                count_B += 1
            elif initChessList[i + m][j - m].value == CHESS_WHITE and count_B == 0:
                count_W += 1
            elif initChessList[i + m][j - m].value == CHESS_WHITE and count_B != 0:
                flags[3] = 1
                break
            elif initChessList[i + m][j - m].value == CHESS_BLACK and count_W != 0:
                flags[3] = 1
                break
        if flags[3] == 0:
            if count_B == 1:
                sum += ONE_BLACK
            elif count_B == 2:
                sum += TWO_BLACK
            elif count_B == 3:
                sum += THREE_BLACK
            elif count_B == 4:
                sum += FOUR_BLACK
            elif count_B == 5:
                sum = FIVE_BLACK
            elif count_W == 1:
                sum += ONE_WHITE
            elif count_W == 2:
                sum += TWO_WHITE
            elif count_W == 3:
                sum += THREE_WHITE
            elif count_W == 4:
                sum += FOUR_WHITE
            elif count_W == 5:
                sum = FIVE_WHITE
            elif count_W == 0 and count_B == 0:
                sum += NOCHESS
    return sum


'''
------------------------------------------------------
函数名：getValue
函数参数：initChessList : 棋盘数组
功能： 计算整个棋盘的评估值
返回值： 返回棋盘的评估值
------------------------------------------------------
'''
def getValue(initChessList):
    sum=0
    for i in range(10):
        for j in range(15):
            sum+=evaluatePoint(initChessList,i,j)
    return sum

'''
------------------------------------------------------
函数名：MaxValue
函数参数：initChessList ：棋盘数组
        depth ：搜索的当前深度
        alpha ：极大极小算法的α值（max父结点）
        beta ：极大极小算法的β值（min父结点）
功能：求子结点最大值
返回值： 子结点的最大值
------------------------------------------------------
'''
def MaxValue(initChessList,depth,alpha, beta):
    global step
    if depth==DEPTH:
        return getValue(initChessList)
    v=-float('inf')
    for temp in initChessList:
        for point in temp:
            if point.value==CHESS_NULL:
                point.value=CHESS_BLACK
                # point.Hvalue=MinValue(initChessList,depth+1,alpha, beta)
                tmp = MinValue(initChessList, depth + 1, alpha, beta)
                if v < tmp:
                    v = tmp
                    step = point
                point.value=CHESS_NULL
                if v>=beta:
                    return v
                alpha=max(alpha,v)
    return v

'''
------------------------------------------------------
函数名：MinValue
函数参数：initChessList ：棋盘数组
        depth ：搜索的当前深度
        alpha ：极大极小算法的α值（max父结点）
        beta ：极大极小算法的β值（min父结点）
功能：求子结点最小值
返回值： 子结点的最小值
------------------------------------------------------
'''
def MinValue(initChessList,depth,alpha, beta):
    global step
    if depth==DEPTH:
        return getValue(initChessList)
    v=float('inf')
    for temp in initChessList:
        for point in temp:
            if point.value==CHESS_NULL:
                tmp=MaxValue(initChessList,depth+1,alpha, beta)
                if v>tmp:
                    v=tmp
                    step=point
                point.value=CHESS_NULL
                if v <= alpha:
                    return v
                beta = min(beta, v)
    return v

'''
------------------------------------------------------
函数名：alpha_beta
函数参数：initChessList ：棋盘数组
功能：求当前局面的最优解，并且在棋盘上标注
返回值： 返回落子的棋子的坐标
------------------------------------------------------
'''
def alpha_beta(initChessList):
    global step
    alpha = -float('inf')
    beta = float('inf')
    v=MinValue(initChessList,0,alpha, beta)#  第0层是输入的棋局，也就是人下完之后的棋局
    step.value=CHESS_WHITE
    print("当前棋局评估值（越大对于黑棋越有利）：", getValue(initChessList))
    return step.x,step.y


