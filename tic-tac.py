"""
File : tic-tac.py
Assignment : Fun/Resume
Language : python3
Author : Michael Rinos < mer8503@g.rit.edu >
Purpose : tic-tac toe game which hopefully will have minamax algorithm 
"""
EMPTY = " "
NUM_SPACES = 10
O = "O"
X = "X"
valid = [0,1,2,3,4,5,6,7,8]

def main():
	"""
	Calls all function to create the game
	"""

	response = str(input("Would you like to go first (y/n): "))
	XorO = str(input("Do you want to be X or O? "))
	if XorO.upper() == X:
		player1 = X
		player2 = O
	else:
		player1 = O
		player2 = X

	board = [EMPTY for i in range(NUM_SPACES)]
	showMoves(copyBoard(board))
	move(board, response, player1)
	print("You have made a move!")

def printBoard(board):
	"""
	Prints an image of the board
	"""
	print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
	print('-----------')
	print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
	print('-----------')
	print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' +str(board[9]))

def copyBoard(board):
	copy = []
	for i in range(NUM_SPACES):
		copy.insert(i,board[i])
	return copy

def showMoves(copy):
	for i in range(NUM_SPACES):
		if copy[i] == EMPTY:
			copy[i] = i
	printBoard(copy)

def gameover(board):
	#the three rows
	if board[0] == board[1] and board[1] == board[2]:
		return True
	if board[3] == board[4] and board[4] == board[5]:
		return True
	if board[6] == board[7] and board[7] == board[8]:
		return True

	#the three colums
	if board[0] == board[3] and board[3] == board[6]:
		return True
	if board[1] == board[4] and board[4] == board[7]:
		return True
	if board[2] == board[5] and board[5] == board[8]:
		return True

	#the diagnols
	if board[0] == board[4] and board[4] == board[8]:
		return True
	if board[2] == board[4] and board[4] == board[6]:
		return True	

	return False

def isTie(board):
	for i in range(NUM_SPACES):
		if board[i] == EMPTY:
			return False
	return True



def move(board, response, player):
	done = False
	while( not done):
		print("Please choose a square to move to, your options are: ")
		showMoves(copyBoard(board))
		move = int(input())
		if move in valid:
			board[move] = player
			valid.remove(move)
			done = True
		else:
			print("That's an invalid move! Choose another spot")

def minamax():
	pass



	

        
main()
