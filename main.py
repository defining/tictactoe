#Tic Tac Toe Game
import sys

board = [' ' for x in range (9)]

def insertLetter(letter, position):
  board[position] = letter

def printBoard(board):
  index = 0
  for row in range(3):
    for i in range(3):
      if (i != 1):
        print('   |   |')
      else:
        print(' ' + board[index] + ' | ' + board[index + 1] + ' | ' + board[index + 2])
        index += 3
    if (i == 2 and row != 2):
      print ('-----------')
        

def isSpaceFree(position):
  return board[position] == ' '

def isWinner(board, letter):
  return ((board[0] == letter and board[1] == letter and board[2] == letter) or
  (board[3] == letter and board[4] == letter and board[5] == letter) or
  (board[6] == letter and board[7] == letter and board[8] == letter) or
  (board[0] == letter and board[3] == letter and board[6] == letter) or
  (board[1] == letter and board[4] == letter and board[7] == letter) or
  (board[2] == letter and board[5] == letter and board[8] == letter) or
  (board[0] == letter and board[4] == letter and board[8] == letter) or
  (board[2] == letter and board[4] == letter and board[6] == letter)
  )

def playerMove():
  run = True
  global board
  while run:
    player = input("Give the position for your next move (between 1 and 9): ")
    try:
      position = int(player)
      if (position < 10 and position > 0):
        if (isSpaceFree(position - 1)):
          insertBoard('X', position)
          run = False
          return 1
        else:
          print("The move is not possible. Choose another one.")
      else:
        print ("Not a number between 1 and 9")
    except:
      print("Enter a real number between 1 and 9")


def selectRandom(list_positions):
    import random
    length = len(list_positions)
    r = random.randrange(0, length)
    return list_positions[r]
   
 
def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ']
    move = 0
   
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
      for i in possibleMoves:  
        boardCopy = board[:]
        boardCopy[i] = let
        if (isWinner(boardCopy, let)):
            move = i
            return move

    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
   
    #Try to take the center
    if 4 in possibleMoves:
        move = 4
        return move
 
    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
 
    return move

def isBoardFull(board):
  if (board.count(' ') > 0):
    return False
  else:
    return True

def insertBoard(letter, position):
    global board
    board[position - 1] = letter


def main():
    #Main game loop
    print("Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.")
    printBoard(board)
 
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("'O's win this time...")
            break
 
       
        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                break
            else:
                insertBoard('O', move + 1)
                print("Computer placed an 'O' in position", move + 1, ":")
                printBoard(board)
        else:
            print("'X's win, good job!")
            break
 
 
    if isBoardFull(board):
        print("Game is a tie! No more spaces left to move.")
try: 
  main()
except KeyboardInterrupt:
  print("")
  print("Thanks for playing.")
  sys.exit(1)
 
while True:
    answer = input("Do you want to play again? (Y/N)")
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(9)]
        print("-----------------------------------")
        main()
    else:
        break