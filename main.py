
from chessGame import *
import pygame  # 导入pygame游戏模块
import time
import sys
from pygame.locals import *

initChessList = []  # 保存的是棋盘坐标
initRole = 1  # 1：代表白棋； 2：代表黑棋
btn_regret_X=650
btn_regret_Y=200
btn_restart_X=650
btn_restart_Y=400

preX=0
preY=0

'''
------------------------------------------------------
函数名：initChessSquare
函数参数：x 坐标横方向的偏移量
        y 坐标纵方向的偏移量
功能： 初始化initChessList这个数组（初始化棋盘）（初始棋子的值都是空）
返回值： 无
------------------------------------------------------
'''
def initChessSquare(x, y):  # 初始化棋盘
    for i in range(15):  # 每一行的交叉点坐标
        rowlist = []
        for j in range(15):  # 每一列的交叉点坐标
            pointX = x + j * 40
            pointY = y + i * 40
            sp = StornPoint(pointX, pointY, CHESS_NULL)
            rowlist.append(sp)
        initChessList.append(rowlist)

'''
------------------------------------------------------
函数名：eventHander
函数参数：无
功能： 监听事件，包括鼠标点击等，然后根据事件修改initChessList的值，然后还要判断落子后的胜负
返回值： 各种事件，宏定义如下
        EVENT_WIN=1
        EVENT_LOSE=2
        EVENT_RESTART=3
        EVENT_REGRET=4
        EVENT_NORMAL=5
------------------------------------------------------
'''
def eventHander():  # 监听各种事件
    global preX, preY
    for event in pygame.event.get():
        global initRole
        if event.type == QUIT:  # 事件类型为退出时
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:  # 当点击鼠标时
            x, y = pygame.mouse.get_pos()  # 获取点击鼠标的位置坐标

            if x<btn_regret_X+240 and x>btn_regret_X and y<btn_regret_Y+60 and y>btn_regret_Y:
                initChessList[preX][preY].value=CHESS_NULL
                return EVENT_REGRET
            elif x<btn_restart_X+240 and x>btn_restart_X and y<btn_restart_Y+60 and y>btn_restart_Y:
                return EVENT_RESTART

            i = 0
            j = 0
            for temp in initChessList:
                for point in temp:
                    if x >= point.x - 10 and x <= point.x + 10 and y >= point.y - 10 and y <= point.y + 10:
                        if point.value == CHESS_NULL and initRole == 1:  # 当棋盘位置为空；棋子类型为黑棋
                            point.value = CHESS_BLACK  # 鼠标点击时，棋子为黑棋
                            preX=i
                            preY=j
                            if judgeResult(i, j, CHESS_BLACK):
                                return EVENT_WIN #  人胜利
                            print("当前棋局评估值（越大对于黑棋越有利）：",getValue(initChessList))
                            return EVENT_NORMAL
                    j += 1
                i += 1
                j = 0
    return 0

'''
------------------------------------------------------
函数名：judgeResult
函数参数：i : 落子的横坐标（数组中的，不是棋盘上的坐标）
        j : 落子的纵坐标（数组中的，不是棋盘上的坐标）
        value : 落子的类型 （CHESS_WHITE=2 , CHESS_BLACK=1）
功能： 判断落子的胜负
返回值： 胜利返回True,否则返回False
------------------------------------------------------
'''
def judgeResult(i, j, value):  # 横向判断
    flag = False
    for x in range(j - 4, j + 5):  # 横向有没有出现5连（在边缘依次逐一遍历，是否五个棋子的类型一样）
        if x >= 0 and x + 4 < 15:
            if initChessList[i][x].value == value and \
                    initChessList[i][x + 1].value == value and \
                    initChessList[i][x + 2].value == value and \
                    initChessList[i][x + 3].value == value and \
                    initChessList[i][x + 4].value == value:
                flag = True
                break

    for x in range(i - 4, i + 5):  # 纵向有没有出现5连（在边缘依次逐一遍历，是否五个棋子的类型一样）
        if x >= 0 and x + 4 < 15:
            if initChessList[x][j].value == value and \
                    initChessList[x + 1][j].value == value and \
                    initChessList[x + 2][j].value == value and \
                    initChessList[x + 3][j].value == value and \
                    initChessList[x + 4][j].value == value:
                flag = True
                break

    # 先判断东北方向的对角下输赢 x 列轴， y是行轴 ， i 是行 j 是列（右斜向）（在边缘依次逐一遍历，是否五个棋子的类型一样）
    for x, y in zip(range(j + 4, j - 5, -1), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15:
            if initChessList[y][x].value == value and \
                    initChessList[y - 1][x + 1].value == value and \
                    initChessList[y - 2][x + 2].value == value and \
                    initChessList[y - 3][x + 3].value == value and \
                    initChessList[y - 4][x + 4].value == value:
                flag = True

    # 2、判断西北方向的对角下输赢 x 列轴， y是行轴 ， i 是行 j 是列（左斜向）（在边缘依次逐一遍历，是否五个棋子的类型一样）
    for x, y in zip(range(j - 4, j + 5), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15:
            if initChessList[y][x].value == value and \
                    initChessList[y + 1][x + 1].value == value and \
                    initChessList[y + 2][x + 2].value == value and \
                    initChessList[y + 3][x + 3].value == value and \
                    initChessList[y + 4][x + 4].value == value:
                flag = True

    if flag:  # 如果条件成立，证明五子连珠
        return True
    return False

'''
------------------------------------------------------
函数名：main
函数参数：无
功能： 联结所有模块，实现人机对弈，同时还要处理一些细节上的问题，如图片位置的设置等
返回值： 无
------------------------------------------------------
'''
# 加载素材
def main():
    global initChessList
    initChessSquare(27, 27)
    pygame.init()  # 初始化游戏环境
    screen = pygame.display.set_mode((920, 620), 0, 0)  # 创建游戏窗口 # 第一个参数是元组：窗口的长和宽
    pygame.display.set_caption("五子棋")  # 添加游戏标题
    background = pygame.image.load("images/bg.png")  # 加载背景图片
    whiteStorn = pygame.image.load("images/storn_white.png")  # 加载白棋图片
    blackStorn = pygame.image.load("images/storn_black.png")  # 加载黑棋图片
    win = pygame.image.load("images/win.png")  # 加载 赢 时的图片
    lose = pygame.image.load("images/lose.png")  # 加载 输 时的图片
    regret = pygame.image.load("images/btn_regret.jpg")  # 加载 悔棋 时的图片
    restart = pygame.image.load("images/btn_restart.jpg")  # 加载 重来 时的图片

    screen.blit(regret, (btn_regret_X, btn_regret_Y))
    screen.blit(restart, (btn_restart_X, btn_restart_Y))

    m, n = 0, 0
    while True:
        screen.blit(background, (0, 0))
        resultFlag = eventHander()  # 调用之前定义的事件函数
        if resultFlag == EVENT_RESTART or resultFlag == EVENT_WIN:
            initChessList = []  # 清空棋盘
            initChessSquare(27, 27)  # 重新初始化棋盘
            if resultFlag==EVENT_WIN:
                screen.blit(win, (60, 200))  # 绘制获胜时的图片
        for temp in initChessList:
            for point in temp:
                if point.value == CHESS_BLACK:  # 当棋子类型为1时，绘制黑棋
                    screen.blit(blackStorn, (point.x - 18, point.y - 18))
                elif point.value == CHESS_WHITE:  # 当棋子类型为2时，绘制白棋
                    screen.blit(whiteStorn, (point.x - 18, point.y - 18))

        pygame.display.update()  # 更新视图

        if resultFlag == EVENT_RESTART or resultFlag == EVENT_WIN:
            time.sleep(3)
            resultFlag = 0  # 置空之前的获胜结果
            continue

        if resultFlag==EVENT_NORMAL:
            m,n=alpha_beta(initChessList)
            screen.blit(whiteStorn, (m - 18, n - 18))
            pygame.display.update()  # 更新视图
            if judgeResult(int((n-27)/40), int((m-27)/40), CHESS_WHITE):
                initChessList = []  # 清空棋盘
                initChessSquare(27, 27)  # 重新初始化棋盘
                screen.blit(lose, (0, 200))  # 绘制失败时的图片
                pygame.display.update()  # 更新视图
                time.sleep(3)
        elif resultFlag==EVENT_REGRET:
            initChessList[int((n-27)/40)][int((m-27)/40)].value=CHESS_NULL
            pass






if __name__ == '__main__':
    main()  # 调用主函数绘制窗口
