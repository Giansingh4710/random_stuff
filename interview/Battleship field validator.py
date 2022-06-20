'''
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

'''
def validate_battlefield(field):
    print(ships(field))
    for i in range(10):
        for j in range(10):
            if field[i][j]==1:
                if field[i+1][j]==1 or field[i-1][j]==1:
                    if field[i][j+1]==1 or field[i][j-1]==1:
                        print(i,j)
                        return False
                    if field[i+1][j+1]==1 or field[i+1][j-1]==1 or field[i-1][j+1]==1 or field[i-1][j-1]==1:
                        return False
    return True

def ships(field):
    streaks=[]
    for i in range(10):
        streak=0
        for j in range(10):
            if field[j][i]==1:
                if field[j][i+1]!=0 or field[j][i-1]!=0:
                    streak+=1
            else:
                if streak!=0:
                    streaks.append(streak)
                    streak=0
    for i in range(10):
        streak=0
        for j in range(10):
            if field[i][j]==1:
                if field[i+1][j]!=0 or field[i-1][j]!=0:
                    streak+=1
            else:
                if streak!=0:
                    streaks.append(streak)
                    streak=0
    return streaks

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))