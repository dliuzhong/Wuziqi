# 显示棋盘
def printBoard(board, x_len, y_len):
    # y 坐标
    print('*|', end='')
    for yy in range(y_len):
        print(str(yy), end='')
        if yy != y_len - 1:
            print('|', end = '')
    print('')
    print('-+', end='')
    for yy in range(y_len):
        print('-', end='')
        if yy != y_len - 1:
            print('+', end = '')
    print('')
    for x in range(x_len):
        for y in range(y_len):
            # x 坐标
            if y == 0:
                print(str(x)+'|', end='')
            print(board[str(x) + '-' + str(y)], end='')
            if y != y_len - 1:
                print('|', end = '')
        print('')
        if x != x_len - 1:
            print('-+', end='')
            for y in range(y_len):
                print('-', end='')
                if y != y_len - 1:
                    print('+', end = '')
            print('')

# 初始化棋盘
def initBoard(board, x_len, y_len):
    for x in range(x_len):
        for y in range(y_len):
            board.setdefault(str(x) + '-' + str(y), ' ')
    return board
# 玩家输入
def playDoInput(whoPlayer):
    print('Player ' + str(whoPlayer))
    pInput = input()
    if pInput == ':q':
        return -1
    while True:
        try:
            inputList = pInput.split()
            inputList[0] = int(inputList[0])
            inputList[1] = int(inputList[1])
            return inputList
        except:
            print('Please input as: 0 0')
            pInput = input()
            continue

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

    
        
myBoardLen = {
    'x': 10,
    'y': 10
}
myBoard = {}            # 棋盘，一个字典
boardPlayOne = []       # 用于判断玩家是否取胜的矩阵
boardPlayTwo = []
initBoard(myBoard, myBoardLen['x'], myBoardLen['y'])
initBoardPlay(boardPlayOne, myBoardLen['x'], myBoardLen['y'])
initBoardPlay(boardPlayTwo, myBoardLen['x'], myBoardLen['y'])
isException = False             # 玩家是否现在异常
exceptionType = -1              # 玩家异常类型，-1无异常
indexBoard = None               # 坐标值
indexPlay = []                # 玩家输入的坐标，-1退出    
turn = 'X'                      # 玩家1 - X, 玩家2 - O
player = 1                      # 玩家1 - 1， 玩家2 - 2
winCondition = 5
printBoard(myBoard, myBoardLen['x'], myBoardLen['y'])
print('If you want to exit, input \':q\'')   
while True:
    indexPlay = playDoInput(player)
    if indexPlay == -1:
        break
    else: 
        try:
            indexBoard = myBoard[str(indexPlay[0]) + '-' + str(indexPlay[1])]
            if indexBoard == 'X' or indexBoard == 'O':
                isException = True
                exceptionType = 1
                print(str(indexPlay[0]) + ',' + str(indexPlay[1]) + ' has value. Try again.')
            else:
                myBoard[str(indexPlay[0]) + '-' + str(indexPlay[1])] = turn 
                isException = False
                exceptionType = -1
                printBoard(myBoard, myBoardLen['x'], myBoardLen['y'])
                if turn == 'X':
                    boardPlayOne[indexPlay[0]][indexPlay[1]] = 1
                    # printBoardPlay(boardPlayOne)
                    if checkWin(boardPlayOne, winCondition) == 1:
                        print('Play 1 win! Game over.')
                        break
                    turn = 'O'
                    player = 2
                else:
                    boardPlayTwo[indexPlay[0]][indexPlay[1]] = 1
                    # printBoardPlay(boardPlayTwo)
                    if checkWin(boardPlayTwo, winCondition) == 1:
                        print('Play 2 win! Game over.')
                        break
                    turn = 'X'
                    player = 1
                
        except:
            print('Please input valid location. Try again.')
            isException = True
            exceptionType = 2
                
    
