board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]
board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]
def nicePrint(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col]==0:
                print("-",end=" ")  #I am doing this because I dont like seeing the 0s I like the - better but it is eaiser to solve if the - is 0 so I just replace it in the print
            else:
                print(puzzle[row][col],end=" ")
            if (col+1)%3==0:
                print("|",end="")
        print()
        if (row+1)%3==0:
            print("-"*25)
    print("\n")
calls=0

def solve(brd):
    global calls
    calls+=1
    for row in range(9):
        for col in range(9):
            if brd[row][col]!=0:
                continue
            for testNum in range(1,10):
                if tryNum(testNum,row,col,brd): # if testNum is valid 
                    brd[row][col]=testNum #replace the 0 with the testNum
                    solvable=solve(brd)
                    if not solvable:
                        brd[row][col]=0
                    else:
                        return True 
            return False #no number fit where there was a zero 
    return True

def solve2(brd):
    def solver(row,col):
        if col==9:
            row+=1
            col=0
        if row==9:
            print("You Win")
            nicePrint(brd)
            return True

        if brd[row][col]==0:
            for i in range(1,10):
                if tryNum(i,row,col,brd):
                    brd[row][col]=i
                    if not solver(row,col+1):
                        brd[row][col]=0
            return False
        else:
            solver(row,col+1)
    solver(0,0)


def tryNum(testNum,row,col,brd):
    if testNum not in brd[row]:
        if testNum not in getCol(col,brd):
            if testNum not in getBox(row,col,brd):
                return True
    return False
def getCol(colNum,brd):
    return [i[colNum] for i in brd]

def getBox(row,col,brd):
    boxNums=[]
    for i in range(3):
        boxNums.append(brd[row][col])
        if col%3==0:
            boxNums.append(brd[row][col+1])
            boxNums.append(brd[row][col+2])
        elif col%3==1:
            boxNums.append(brd[row][col-1])
            boxNums.append(brd[row][col+1])
        elif col%3==2:
            boxNums.append(brd[row][col-2])
            boxNums.append(brd[row][col-1])

        if row%3==0:
            row+=1
        elif row%3==1:
            row+=1
        elif row%3==2:
            row-=2
    return boxNums

nicePrint(board)
solve(board)
nicePrint(board)