#Tic Tac Toe Game

board = [' ' for x in range (9)]

def insertLetter(letter, position):
  board[position] = letter

def printBoard(board):
  for i in range(3):
    for j in range(3):
      print('  ',end=" ")
      if j != 2:
        print('|', end="")
      if j == 2:
        print("")
    print(' ' + board[i] + ' | ' + board[i + 1] + ' | ' + board[i + 2])
    print('   |   |')
    if i != 2:
      print ('-----------')

def isSpaceFree(position):
  return board[position] == ' '

def selectRandom(board): 
  pass

def isWinner(board, letter):
  pass

def playerMove():
  pass

def computerMove():
  pass

def isBoardFull(board):
  pass

def main():
  printBoard(board)

main()