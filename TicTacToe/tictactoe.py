import random

board= ["_","_","_",
        "_","_","_",
        "_","_","_"]

Current_Player ="X"
winner= None
gameRunning = True

# Printing the Game Board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take Player Input

def playerInput(board):
    inp = int(input("Enter a Number 1-9: =>   "))
    if inp >= 1 and inp <=9 and board[inp-1] == "_":
        board[inp-1] = Current_Player
        
    else: 
        print("OOps. Playing ")


# Check for win or tie

## Win Rule in Colum

def checkColum(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

## Win Rule in Row    

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return 
    
## Win Rule in Diagonal

def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] !="_":
        winner = board[6]
        return True
    
    
    
def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("Tie")
        gamerunning = False
        
def checkWin():
    if checkColum(board) or checkdiag(board) or checkRow(board):
        print(f"You won Dear  {winner}")

# Switch the Player

def SwitchPlayer():
    global Current_Player
    if Current_Player == "X":
        Current_Player = "0"
    else:
        Current_Player= "X"
    
    
# Computer play 

def computer(board):
    while Current_Player == "0":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "0"
            SwitchPlayer()


# Check for win or tie Again 

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    SwitchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
    