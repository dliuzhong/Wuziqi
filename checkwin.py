
# 判断当前的array是否胜利
# property: boardArray - Array[][] - 玩家的操作数组
#           condition - int - 胜利条件
# return: -2 异常， -1 boardArray void, 0 没有胜利, 1 胜利
def checkWin(boardArray, condition):
    try:
        y_len = len(boardArray)
        if y_len <= 0 or y_len < condition :
            return -1
        x_len = len(boardArray[0])
        if x_len <= 0 or x_len < condition:
            return -1
        value = 0
        for y in range(y_len - condition + 1):
            for x in range(x_len - condition + 1):
                # 第一种判断
                value = 1 
                for cd in range(condition):
                    value *= boardArray[y][cd+x]
                    if value == 0:
                        break
                if value == 1:
                    return 1
                # 第二种判断
                value = 1
                for cd in range(condition):
                    value *= boardArray[cd+y][x]
                    if value == 0:
                        break
                if value == 1:
                    return 1
                # 第三种判断
                value = 1
                for cd in range(condition):
                    value *= boardArray[cd+y][cd+x]
                    if value == 0:
                        break
                if value == 1:
                    return 1
                # 第四种判断
                value = 1
                for cd in range(condition):
                    value *= boardArray[cd+y][condition - cd - 1 + x]
                    if value == 0:
                        break
                if value == 1:
                    return 1
                # 第五种判断
                value = 1
                for cd in range(condition):
                    value *= boardArray[cd+y][condition - 1 + x]
                    if value == 0:
                        break
                if value == 1:
                    return 1
                # 第六种判断
                value = 1
                for cd in range(condition):
                    value *= boardArray[condition - 1 + y][cd+x]
                    if value == 0:
                        break
                if value == 1:
                    return 1
        return 0
    except:
        return -2
def initBoardPlay(board, x_len, y_len):
    for y in range(y_len):
        tList = []
        for x in range(x_len):
            tList += [0]
        board += [tList]
def printBoardPlay(board):
    print('array:')
    for y in range(len(board)):
        for x in range(len(board[y])):
            print(str(board[y][x]), end='')
        print('')

board = []
initBoardPlay(board, 3, 3)
board[2][0] = 1
board[2][1] = 1
board[2][2] = 1
printBoardPlay(board)
print(str(checkWin(board, 3)))