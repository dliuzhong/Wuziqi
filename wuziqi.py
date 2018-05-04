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
    for x in range(x_len):
        tList = []
        for y in range(y_len):
            tList += [0]
        board += [tList]
def printBoardPlay(board):
    print('array:')
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(str(board[x][y]), end='')
        print('')
        
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
printBoard(myBoard, myBoardLen['x'], myBoardLen['y'])
print('If you want to exit, input \':q\'')
exceptionPlayerOne = False     # 玩家1是否现在异常
exceptionPlayerOneType = -1    # 玩家1异常类型，-1无异常
exceptionPlayerTwo = False     # 玩家2是否现在异常
exceptionPlayerTwoType = -1    # 玩家2异常类型，-1无异常
indexBoard = None              # 坐标值
iOnePlayer = []                # 玩家1输入的坐标，-1退出
iTwoPlayer = []                # 玩家2输入的坐标，-1退出            
while True:
    if not exceptionPlayerTwo:
        iOnePlayer = playDoInput(1)
        if iOnePlayer == -1:
            break
        else: 
            try:
                indexBoard = myBoard[str(iOnePlayer[0]) + '-' + str(iOnePlayer[1])]
                if indexBoard == 'X' or indexBoard == 'O':
                    exceptionPlayerOne = True
                    exceptionPlayerOneType = 1
                else:
                    myBoard[str(iOnePlayer[0]) + '-' + str(iOnePlayer[1])] = 'X' 
                    boardPlayOne[iOnePlayer[0]][iOnePlayer[1]] = 1
                    exceptionPlayerOne = False
                    exceptionPlayerOneType = -1
                    printBoard(myBoard, myBoardLen['x'], myBoardLen['y'])
                    printBoardPlay(boardPlayOne)
            except:
                print('Please input valid location. Try again.')
                exceptionPlayerOne = True
                exceptionPlayerOneType = 2
    elif exceptionPlayerTwoType == 1:
        print(str(iTwoPlayer[0]) + ',' + str(iTwoPlayer[1]) + ' shas value. Try again.')
    if not exceptionPlayerOne:
        iTwoPlayer = playDoInput(2)
        if iTwoPlayer == -1:
            break
        else:
            try:
                indexBoard = myBoard[str(iTwoPlayer[0]) + '-' + str(iTwoPlayer[1])]
                if indexBoard == 'O' or indexBoard == 'X':
                    exceptionPlayerTwo = True
                    exceptionPlayerTwoType = 1
                else:
                    myBoard[str(iTwoPlayer[0]) + '-' + str(iTwoPlayer[1])] = 'O'
                    boardPlayTwo[iTwoPlayer[0]][iTwoPlayer[1]] = 1
                    exceptionPlayerTwo = False
                    exceptionPlayerTwoType = -1
                    printBoard(myBoard, myBoardLen['x'], myBoardLen['y'])
                    printBoardPlay(boardPlayTwo)
            except:
                print('Please input valid location. Try again.')
                exceptionPlayerTwo = True
                exceptionPlayerTwoType = 2
    elif exceptionPlayerOneType == 1:
        print(str(iOnePlayer[0]) + ',' + str(iOnePlayer[1]) + ' has value. Try again.')
                
    
