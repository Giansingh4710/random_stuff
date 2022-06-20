import turtle
import random

CELL_SIZE = 100  # This may be adjusted, depending on screen resolution

# Gridlines, two vertical and two horizontal, in (begin, end) format
VERT_LEFT = (
    (-CELL_SIZE/2, CELL_SIZE*3/2),   # start point 
    (-CELL_SIZE/2, -CELL_SIZE*3/2)   # end point
    )
VERT_RIGHT = (
    (CELL_SIZE/2, CELL_SIZE*3/2),    # start point 
    (CELL_SIZE/2, -CELL_SIZE*3/2)    # end point
    )
HORZ_TOP = (
    (-CELL_SIZE*3/2, CELL_SIZE/2),     # start point 
    (CELL_SIZE*3/2, CELL_SIZE/2)       # end point
    )
HORZ_BOTTOM = (
    (-CELL_SIZE*3/2, -CELL_SIZE/2), # start point 
    (CELL_SIZE*3/2, -CELL_SIZE/2)   # end point
    )

CELL_CENTERS = (
    (-CELL_SIZE, CELL_SIZE),   # cell 0 center (x, y)
    (0, CELL_SIZE),            # cell 1 center (x, y)
    (CELL_SIZE, CELL_SIZE),    # cell 2 center (x, y)
    (-CELL_SIZE, 0),           # cell 3 center (x, y)
    (0, 0),                    # cell 4 center (x, y)
    (CELL_SIZE, 0),            # cell 5 center (x, y)
    (-CELL_SIZE, -CELL_SIZE),  # cell 6 center (x, y)
    (0, -CELL_SIZE),           # cell 7 center (x, y)
    (CELL_SIZE, -CELL_SIZE)    # cell 8 center (x, y)
    )

TRIPLETS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 3 horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 3 vertical
    (0, 4, 8), (2, 4, 6)              # 2 diagonal
    )

NUM_TRIPLETS = len(TRIPLETS)

def initTurtle(t, use):
    ''' Set turtle attributes for various drawing tasks. 
    '''
    if use == 'drawGrid':
        t.hideturtle()
        t.width(20)
        t.color('black')
        t.speed('fastest')
    elif use == 'drawX':
        t.hideturtle()
        t.width(20)
        t.color('green')
        t.speed('fastest')
    elif use == 'drawO':
        t.hideturtle()
        t.width(20)
        t.color('blue')
        t.speed('fastest')
    elif use == 'labelCells':
        t.hideturtle()
        t.color('black')
        t.speed('fastest')
    elif use == 'drawWinLine':
        t.hideturtle()
        t.width(30)
        t.color('red')
        t.speed('fastest')
    elif use == 'showExitMessage':
        t.hideturtle()
        t.width(60)
        t.color('red')
        t.speed('fastest')

def drawLine(t, startpoint, endpoint):
    ''' startpoint and endpoint are (x,y) coordinate pairs '''
    t.up()
    t.goto(startpoint[0], startpoint[1])
    t.down()
    t.goto(endpoint[0], endpoint[1])

def drawGrid(t):
    ''' Draw two vertical and two horizontal grid lines 
    '''
    initTurtle(t, 'drawGrid')
    
    # vertical gridlines
    drawLine(t, VERT_LEFT[0], VERT_LEFT[1])
    drawLine(t, VERT_RIGHT[0], VERT_RIGHT[1])

    # horizontal gridlines
    drawLine(t, HORZ_TOP[0], HORZ_TOP[1])
    drawLine(t, HORZ_BOTTOM[0], HORZ_BOTTOM[1])    


def drawX(t, cell):
    ''' Draw an 'X' in the specified cell. 
    '''
    initTurtle(t, 'drawX')

    t.up()
    midpoint = CELL_CENTERS[cell]
    t.goto(midpoint[0], midpoint[1])
    t.setheading(135)
    drawLineMidpoint(t, CELL_SIZE*.8)
    t.setheading(45)
    drawLineMidpoint(t, CELL_SIZE*.8)

def testX(t):
    ''' Draw an X in each of the 9 grid cells '''
    for i in range(9):
        drawX(t, i)


def drawLineMidpoint(t, length):
    ''' Draw a line of specified length. t is initially at the midpoint 
    of the line and oriented in the direction of the line.
    '''
    t.up()
    t.fd(length/2)
    t.down()
    t.bk(length)
    t.up()
    t.fd(length/2)

def concentricCircle(t, radius):
    '''Draw a circle of given radius centered at initial location of t.
    Leave t at initial location and orientation on return.
    '''
    t.up()
    t.fd(radius)
    t.left(90)
    t.down()
    t.circle(radius)
    t.right(90)
    t.up()
    t.back(radius)
    
def drawO(t, cell):
    ''' Draw a concentric circle (an 'O') in the specified cell. '''
    initTurtle(t, 'drawO')
    radius = CELL_SIZE/3.5    
    t.up()
    t.goto(CELL_CENTERS[cell])
    t.left(90)
    concentricCircle(t, radius)

def testO(t):
    ''' Draw an O in each of the 9 grid cells '''
    for i in range(9):
        drawO(t, i)

def labelCell(t, cell):
    ''' Use turtle t to write the number in the middle of cell (an int 0-8) '''
    t.up()
    t.goto(CELL_CENTERS[cell])
    t.down()
    t.write(cell, font=("Arial", 10, "bold"))

def labelCells(t):
    ''' Label cells 0 through 8 at their midpoints'''
    initTurtle(t, 'labelCells')

    for i in range(9):
        labelCell(t, i)

def getMove(s, player, board):
    ''' Use turtle screen method to get player input.
             s: a screen
             player: 'X' or 'O'. 
             board: a list of 9 cell values -- 'X', 'O' or '-'. 
    Return a legal move. I.e., in range 0-8 such that board[move] == '-'.
    '''
    msg = player + ', pick a cell to move'
    while True:
        move = s.numinput("", msg, default=None, minval=0, maxval=8)
        #if user clicks cancel the program crashes due to TypeError for int()
        if move is None:
            msg = 'You must choose a valid move'
            continue
        intMove = int(move)
        if board[intMove] == '-':
            return intMove
        msg = 'Not a valid move. Try again.'

def testGetMove(iterations):
    s = turtle.Screen()

    for i in range(iterations):
        t = turtle.Turtle()
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # 9 empty cells

        drawGrid(t)
        labelCells(t)

        # pick random moves (a win is not excluded)
        numMoves = random.randint(0,8)
        for i in range(numMoves):
            if i%2 == 0:
                randmove = 'X'
            else:
                randmove = 'O'
            board[i] = randmove
        random.shuffle(board)
        
        # display the game
        drawGrid(t)
        for cell in range(len(board)):
            if board[cell] == 'X':
                drawX(t, cell)
            elif board[cell] == 'O':
                drawO(t, cell)

        # call getMove
        if numMoves%2 == 0:
            player = 'X'
        else:
            player = 'O'
        move = getMove(s, player, board)

        # validate move with 2 tests
        if move not in range(9):
            print('FAIL', 'must be an int in 0-8')
            break
        if board[move] != '-':
            print('FAIL', 'must move in an empty cell')
            break
        print('PASS')
        s.clear()
        t = turtle.Turtle()

def drawWinLine(t, triplet):
    ''' Draw a line connecting the centers of the first and third cells
    of a winning triplet. 
    '''
    # Initialize the turtle for drawWinLine
    initTurtle(t, 'drawWinLine')

    # Draw the win line by calling drawLine. Identify the
    # startCell and endCell for the win line. Create variables
    # startPoint and endPoint, using the data in CELL_CENTERS
    # (4 lines if you do one thing per line)
    startCell, endCell = triplet[0], triplet[2]
    startCenter = CELL_CENTERS[startCell]
    endCenter = CELL_CENTERS[endCell]
    drawLine(t, startCenter, endCenter)

def testDrawWinLine():
    ''' Test the function drawWinLine by drawing a TTT grid
    then drawing all possible win lines on it.
    '''
    # Create a screen and turtle (two lines)
    s = turtle.Screen()
    t = turtle.Turtle()

    # Draw the TTT grid (one line)
    drawGrid(t)

    # Call drawWinLine once for each triplet in TRIPLETS
    for triplet in TRIPLETS:
        drawWinLine(t, triplet)

    # Pause the graphics screen
    s.exitonclick()


def isWin(t, board, player):
    ''' If player has three in a row, draw a win line and return TRUE.
    Otherwise, return FALSE.
    '''
    for triplet in TRIPLETS:
        a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
        if a == b == c == player:
            drawWinLine(t, triplet)
            return True
    return False

def testIsWin(iterations):
    ''' Generate iterations number of TTT games. Chose each move at random
    from among the empty cells. After each move, determine whether a win has
    occurred, and check whether isWin provides the same answer. Print PASS or
    FAIL message, and exit on FAIL.
    '''
    s = turtle.Screen()
    print('\ntesting isWin')

    # loop through the games
    for i in range(iterations):
        t = turtle.Turtle()
        t.hideturtle()
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # 9 empty cells
        empty = [0, 1, 2, 3, 4, 5, 6, 7, 8] # indices of empty cells
        drawGrid(t)

        # in each game, make random moves until board is full or a win
        player, nextPlayer = 'X', 'O'
        while '-' in board:
            move = random.choice(empty)
            empty.remove(move)
            board[move] = player
            if player == 'X':
                drawX(t, move)
            else:
                drawO(t, move)

            win = False
            for triplet in TRIPLETS:
                a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
                if a == b == c == player:
                    win = True
            # compare testWin to isWin       
            if win != isWin(t, board, player):
                print('FAIL', board, 'win =', win)
                return   # end test on FAIL
            if win == True:
                break # go to next game
            player, nextPlayer = nextPlayer, player # next move

        # next game
        if win == True:
            print('PASS', board, 'win')
        else:
            print('PASS', board, 'draw')
        s.clear()
        t = turtle.Turtle()

#testIsWin(25)

def isDraw(board):
    ''' A TRIPLET is blocked (not available for a win by either player)
    if it contains at least 1 cell of each player. If all TRIPLETs are blocked
    return True, else return FALSE. (Note: this does not preclude some other
    more sensitive formula from detecting additional draws.)
    '''
    for triplet in TRIPLETS:
        a,b,c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
        if not ('X' in (a,b,c) and 'O' in (a,b,c)):
            return False
    return True

def testIsDrawGame():
    ''' Generate a TTT game by choosing each move at random from among
    the empty cells. Terminate when the game is won. After each move, 
    if the game is not won, compare the board evaluation of testIsDraw to
    the evaluation of isDraw. Print PASS if they agree, FAIL otherwise. 
    Halt the testing on FAIL.
    '''
    board = ['-','-','-','-','-','-','-','-','-'] # 9 empty cells
    empty = [0, 1, 2, 3, 4, 5, 6, 7, 8] # indices of empty cells
    player, nextPlayer = 'X', 'O'

    # the game loop
    moveCount = 0
    while '-' in board:
        # make a move
        move = random.choice(empty)
        empty.remove(move)
        board[move] = player
        moveCount += 1

        # check for win. In case of win, terminate game
        for triplet in TRIPLETS:
            a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
            if a == b == c != '-':
                print('GAME OVER', a, 'wins')
                return

        # check for draw
        blocked = 0
        for triplet in TRIPLETS:
            a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
            if 'X' in (a,b,c) and 'O' in (a,b,c):
                blocked += 1
        testDraw = (blocked == NUM_TRIPLETS)
        drawn = isDraw(board)

        if testDraw != drawn:  # testIsDraw finds error in isDraw
            print('FAIL', board, 'moves', moveCount, ', testDraw', testDraw, ', isDraw', drawn)
            return
        else: # testIsDraw confirms isDraw
            print('PASS', board, 'moves', moveCount, ', testDraw', testDraw, ', isDraw', drawn)

        player, nextPlayer = nextPlayer, player

def testIsDrawGames(iterations):
    print('\ntesting isDraw')
    for i in range(iterations):
        print('Game', i)
        testIsDrawGame()

#testIsDrawGames(25)

def drawMove(t, player, cell):
    ''' Call drawX if player is 'X' or drawO if player is 'O' to 
    draw a move in cell
    '''
    if player == 'X':
        drawX(t, cell)
    elif player == 'O':
        drawO(t, cell)

def showExitMessage(t, winner):
    ''' The game is over; write outcome message '''

def playTicTacToe():
    '''Initialize the board and the game. Alternate play between 
    X and O, X going first, until the board is full. Check for a win 
    after each move and end play in case of a win. Terminate with a 
    Win/Draw message.
    '''
    # create screen and turtle
    s = turtle.Screen()
    t = turtle.Turtle()

    # draw the board 
    drawGrid(t)
    labelCells(t)
    
    # initialize the game
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # 9 empty cells
    winner = None
    player, nextPlayer = 'X', 'O'  # The rule is, X goes first

    ''' Loop through moves. After each move, check if the game is won or drawn. 
    If won, set winner. Break on win or draw. Otherwise, switch players and 
    continue to next move.
    '''
    while '-' in board:  # a legal move is still available
        move = getMove(s, player, board) 
        board[move] = player # update board to reflect the latest move
        if player == 'X':
            drawX(t, move)
        else:
            drawO(t, move)
        
        if isWin(t, board, player):
            winner = player
            break
        
        if isDraw(board):
            break

        # If there's no win or draw, play continues
        player, nextPlayer = nextPlayer, player # alternate player 

    # show exit message
    s.exitonclick()

playTicTacToe()









