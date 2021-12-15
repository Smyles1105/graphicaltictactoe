#Tic Tac Toe Game using the graphics file made by John Zelle

from graphics import *
board = ["  " for x in range(10)]

def insertBoard(letter, pos):
        board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == "  "

def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def getCoords(window):
    doneTurn = False
    while doneTurn == False:  # Get user input
        mouse = window.getMouse()
        if mouse is not None:
            coordinates = mouse.getX(), mouse.getY()
            doneTurn = True
            if coordinates[0] > 580 and coordinates[1] < 50:
                window.close()
                quit()
    return coordinates

def getQuadrant(coords):
    if coords[1] < 250:
        column = 0
    elif coords[1] < 450:
        column = 1
    else:
        column = 2

    if coords[0] < 200:
        row = 0
    elif coords[0] < 400:
        row = 1
    else:
        row = 2

    positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    quadrant = positions[row][column]
    return [quadrant, row, column]


def playerMove(window, title):
    run = True
    while run:
            coords = getCoords(window)
            move = getQuadrant(coords)
            try:
                if move[0] > 0 and move[0] < 10:
                    if spaceIsFree(move[0]):
                        run = False
                        return move
                    else:
                        title.setText("Position isn't free, please try again.")
                else:
                    title.setText("Position isn't valid, please try again.(Cannot click on title/error text)")
            except:
                title.setText("Position isn't valid, please try again.(Cannot click on title/error text)")

def selectRandom(li):
    import random
    line = len(li)
    r = random.randrange(0,line)
    return li[r]

def compMove():
    possibleMoves = []
    for x, letter in enumerate(board):
        if letter == "  " and x != 0:
            possibleMoves.append(x)
    move = 0
    #the first loop is so that it checks if there are winning moves for either player
    #with preference for computer winning moves as it's the computer.
    for l in ['O', 'X']:
        #this loop iterates through the possible moves available.
        for i in possibleMoves:

            boardCopy = board[:]
            boardCopy[i] = l
            if isWinner(boardCopy, l):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen)
            return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
    return move

def isBoardFull(board):
    if board.count("  ") > 1:
        return False
    else:
        return True

def createBoard(win):
    # Vertical Boundaries
    boundaryLine1 = Line(Point(210, 50), Point(210, 680))
    boundaryLine1.setWidth(15)
    boundaryLine1.draw(win)

    boundaryLine2 = Line(Point(420, 50), Point(420, 680))
    boundaryLine2.setWidth(15)
    boundaryLine2.draw(win)

    # Horizontal Boundaries
    boundaryLine3 = Line(Point(0, 250), Point(630, 250))
    boundaryLine3.setWidth(15)
    boundaryLine3.draw(win)

    boundaryLine4 = Line(Point(0, 475), Point(630, 475))
    boundaryLine4.setWidth(15)
    boundaryLine4.draw(win)

def drawMove(move, player, win):
    centerPoint = Point(105 + (move[1] * 210), 151 + (move[2] * 215))
    if player == "O":
        radius = 75

        moveDrawing = Circle(centerPoint, radius)
        moveDrawing.setWidth(5)
        moveDrawing.setOutline("white")
        moveDrawing.draw(win)
        outerOutline = Circle(centerPoint, radius+3)
        outerOutline.setOutline("blue")
        outerOutline.setWidth(3)
        outerOutline.draw(win)
        innerOutline = Circle(centerPoint, radius - 3)
        innerOutline.setOutline("blue")
        innerOutline.setWidth(3)
        innerOutline.draw(win)
    else:

        moveDrawing = Text(centerPoint, "X")
        moveDrawing.setSize(36)
        moveDrawing.setOutline("green")
        moveDrawing.draw(win)


def main():
    win = GraphWin("Tic Tac Toe", 630, 680)

    # Title
    title = Text(Point(300, 25), "TIC TAC TOE")
    title.setSize(24)
    title.draw(win)
    createBoard(win)
    quitBtn = Text(Point(605, 27.5), "X")
    quitBtn.setSize(25)
    quitBtn.setTextColor("red")
    quitBtn.draw(win)
    quitBtnBox = Rectangle(Point(580, 3), Point(630, 50))
    quitBtnBox.setWidth(3)
    quitBtnBox.setOutline("red")
    quitBtnBox.draw(win)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            move = playerMove(win, title)
            insertBoard('X', move[0])
            drawMove(move, "X", win)
        else:
            title.setText("O wins this time")
            break

        if not(isWinner(board, "X")):
            move = compMove()
            positions = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
            for x in range(1, 4):
                for y in range(1, 4):

                    if move == positions[x-1][y-1]:
                        quadrant = ["", x-1, y-1]
                        break


            if move == 0:
                title.setText("Game is a Tie!")
            else:
                insertBoard('O', move)
                drawMove(quadrant, "O", win)
        else:
            title.setText("You win!")

            break

    if isBoardFull(board):
        if not(isWinner(board, "X") and isWinner(board, "O")):
            title.setText("Game is a tie.")

    qt = False
    if qt == True:
        win.close()
    else:
        while qt == False:
            inp = win.getMouse()
            print(inp)
            if inp.getY() < 50 and inp.getX() > 580:
                qt = True
main()
