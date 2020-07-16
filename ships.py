# (C) Aran Roig, 2020
import string
import time

# Funcio per inicialitzar el taulell
def startBoard():
    board = []
    for x in range(0, 5):
        row = []
        for y in range(0, 5):
            row.append('W')
        board.append(row)
    return board

# Funcio per mostrar el taulell
def showBoard(board):
    for x in board:
        for y in x:
            print(y, end = '')
        print ('\n', end = '')

# Funcio per saber el final de la partida
def final(board):
    for s in board:
        if 'S' in s:
            return False
    return True

# Funcio per comprobar el format "A:B" 
numbers = ['0','1','2','3','4']
def thereIsNoNumber(s):
    if(len(s) != 3):
        return True
    if(s[0] in numbers and s[2] in numbers):
        return False
    return True

# Funcio per saber si una casella del taulell equival a la que poses en char
def checkBox(board, coord, char):
    x, y = coord
    if(board[x][y] == char):
        return True
    else:
        return False

# Funcio per saber si es poden colocar vaixells
#
#def someBoxOccupied(board, x, y, o):
#    c1 = (x, y)
#    
#    if o == 'H':
#        if(x + 2 > 4 or x < 0):
#            return False
#        c2 = (x + 1, y)
#        c3 = (x + 2, y)
#    elif o == 'V':
#        if(y + 2 > 4 or y < 0):
#            return False 
#       c2 = (x, y - 1)
#        c3 = (x, y - 2)
#    if(checkBox(board, c1, 'W') and checkBox(board, c2, 'W') and checkBox(board, c3, 'W')):
#        return True
#    return False

# Funcio per convertir "A:B" a tuple
def getCoords(shoot):
    if thereIsNoNumber(shoot):
        return None
    # Aixo es mes easy a C++
    return (ord(shoot[0]) - ord('0'), ord(shoot[2]) - ord('0'))

def someBoxOccupied(b,x,y,o):
    if x>=3 and o=='V':
        return True
    elif y>=3 and o=='H':
        return True
    if o == 'V':
        if b[x][y] == 'W' and b[x+1][y] == 'W' and b[x+2][y] == 'W':
            return False
        else:
            return True
    elif o == 'H':
        if b[x][y] == 'W' and b[x][y+1] == 'W' and b[x][y+2] == 'W':
            return False
        else:
            return True

# Funcio per assignar un valor a una coord del taulell
def setBoard(board, coords, char):
    board[coords[0]][coords[1]] = char
    return board

# Funcio per aplicar una jugada a un tuple de coordenades
def applyPlay(board, shoot):
    coords = getCoords(shoot)
    if(coords is None):
        print ("Internal error")
        return None
    x, y = coords
    if(board[x][y] in ['X', 'O']):
        print("This box has already been played! You've missed a shot!")
        return board
    if(board[x][y] == 'S'):
        print("IMPACT!")
        return setBoard(board, (x, y), 'O')
    if(board[x][y] == 'W'):
        print("WATER!")
        return setBoard(board, (x, y), 'X')
    print ("Internal error")
    return board

def getOrientation():
    o = input("Would you like to place the boat vertically or horizontally? (v / h) ")
    o = o.upper()
    while o != 'V' and o != 'H':
        print("Sorry, this in not a valid option.")
        o = input("Would you like to place the boat vertically or horizontally? (v / h) ")
        o = o.upper()
    return o


def getPosition():
    pos = input("Initial box [row:column from 0 to 4]: ")
    while thereIsNoNumber(pos):
        print("Sorry, this is not a valid position.")
        pos = input("Initial box [row:column from 0 to 4]: ")
    return pos

def getAttackPosition():
    pos = input("Where do you want to shoot? [row:column from 0 to 4]: ")
    while thereIsNoNumber(pos):
        print("Sorry, this is not a valid position.")
        pos = input("Where do you want to shoot? [row:column from 0 to 4]: ")
    return pos

def placeShip3(b, i):
    pos = getPosition()
    l = pos.split(":")
    x = int(l[0])
    y = int(l[1])
    o = getOrientation()
    while someBoxOccupied(b, x, y, o):
        print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again")
        pos = getPosition()
        l = pos.split(":")
        x = int(l[0])
        y = int(l[1])
        o = getOrientation()
    if o == "V":
        b[x][y] = "S"
        b[x+1][y] = "S"
        b[x+2][y] = "S"
    else:
        b[x][y] = "S"
        b[x][y+1] = "S"
        b[x][y+2] = "S"
    return b

def placeShips(board):
    showBoard(board)
    print("You have 3 boats of 3 positions")
    for i in range(1,4):
        print("Reading the 3 positions ship number " + str(i))
        board = placeShip3(board, i)
        showBoard(board)
    return board


def line():
    return "-" * 30

def clear():
    for i in range(0, 50):
        print("")
    return

## TESTUS
def play():
    #Inicialitzar taulells!
    
    b1 = startBoard()
    b2 = startBoard()

    print("Welcome to warship.py! The best game of the brunomoya series!")
    print("DISCLAIMER: This game is sponsored by glassear and RAID: Shadow Legends")

    # j1 posa conos
    print(line())
    print("Player 1 you have to put your ships!")
    print(line())

    

    

    b1 = placeShips(b1)

    clear()
    print("These are now your ships:")
    showBoard(b1)
    
    time.sleep(3)

    clear()

    print(line())
    print("Player 2 you have to put your ships!")
    print(line())

    b2 = placeShips(b2)

    clear()
    print("These are now your ships:")
    showBoard(b2)

    time.sleep(3)

    clear()

    print(line())
    
    turn = 1

    beforeMessage = ""

    while(True):
        print(line())
        print("Turn " + str(turn))
        print("Player 1 moves now")
        print(line())
        print("Your board:")
        showBoard(b1)
        print(line())
        # Torn del j1
        
        b2 = applyPlay(b2, getAttackPosition())

        time.sleep(2)

        clear()

        if(final(b2)):
            break

        print(line())
        print("Turn " + str(turn))
        print("Player 2 moves now")
        print(line())
        print("Your board:")
        showBoard(b2)
        print(line())
        # Torn del j2
        
        b1 = applyPlay(b1, getAttackPosition())

        time.sleep(2)

        clear()

        if(final(b1)):
            break

        turn = turn + 1

    if(final(b2)):
        print("PLAYER 1 WON! WEEEEEEEEEEEEEEEEE")
    elif(final(b1)):
        print("PLAYER 2 WON! WOOOOOOOOHOOOOOOOO")
    else:
        print("WAT JUST HAPPENED NOBODY WOOON!")

play()
