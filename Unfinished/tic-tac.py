"""
File : tic-tac.py
Assignment : Fun/Resume
Language : python3
Author : Michael Rinos < mer8503@g.rit.edu >
Purpose : tic-tac toe game which hopefully will have minamax algorithm 
"""
from decimal import Decimal

EMPTY = " "
NUM_SPACES = 9
O = "O"
X = "X"
valid = [1,2,3,4,5,6,7,8,9]

def main():
	"""
	Calls all function to create the game
	"""

	pleyComputer = str(input("Do you want to play the Computer (y/n): "))
	XorO = str(input("Do you want to be X or O? "))
	goFirst = str(input("Would you like to go first (y/n): "))
	board = [EMPTY for i in range(NUM_SPACES)]
	if XorO.upper() == X:
		player1 = X
		player2 = O
	else:
		player1 = O
		player2 = X

	printBoard(board)
	if pleyComputer.lower() == 'n':
		if goFirst.lower() == "y":
			while not gameOver(board, player2) or not isTie(board):
				move(board, player1)
				if gameOver(board, player1) or isTie(board):
					break;
				move(board,player2)
		else:
			while not gameOver(board, player1) or not isTie(board):
				move(board, player2)
				if gameOver(board, player2) or isTie(board):
					break;
				move(board, player1)
	else:
                if goFirst.lower() == "y":
			while not gameOver(board, player2) or not isTie(board):
				move(board, player1)
				if gameOver(board, player1) or isTie(board):
					break;
				computerMove(board,player2)
		else:
			while not gameOver(board, player1) or not isTie(board):
				computerMove(board,player2)
				if gameOver(board, player2) or isTie(board):
					break;
				move(board, player1)	
		
	print("Game Over")

def printBoard(board):
	"""
	Prints an image of the board
	"""
	print(' ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
	print('-----------')
	print(' ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
	print('-----------')
	print(' ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' +str(board[8]))

def copyBoard(board):
	copy = []
	for i in range(NUM_SPACES):
		copy.insert(i,board[i])
	return copy

def showMoves(copy):
	for i in range(1,NUM_SPACES+1):
		if copy[i-1] == EMPTY:
			copy[i-1] = i
	printBoard(copy)

def gameOver(board, player):
	#the three rows
	if board[0] == player and board[1] == player and board[2] == player:
		return True
	if board[3] == player and board[4] == player and board[5] == player:
		return True
	if board[6]== player and board[7] == player and board[8] == player:
		return True

	#the three colums
	if board[0]== player and board[3] == player and board[6] == player:
		return True
	if board[1]== player and board[4] == player and board[7] == player:
		return True
	if board[2]== player and board[5] == player and board[8] == player:
		return True

	#the diagnols
	if board[0]== player and board[4] == player and board[8] == player:
		return True
	if board[2]== player and board[4] == player and board[6] == player:
		return True	

	return False

def isTie(board):
	for i in range(NUM_SPACES):
		if board[i] == EMPTY:
			return False
	return True



def move(board, player):
	done = False
	while( not done):
		print("Please choose a square to move to, your options are: ")
		showMoves(copyBoard(board))
		move = int(input())
		if move in valid:
			board[move-1] = player
			valid.remove(move)
			done = True
		else:
			print("That's an invalid move! Choose another spot")

def computerMove(board, player):
	copy = copyBoard(board)
	print(player)
	move = minamax(copy, 2,True, player)
	print("this is the move: ")
	print(move)

def minamax(board, depth, maximizingPlayer, player):
	if depth == 0:
		return value(board,player)
	if maximizingPlayer:
		bestValue = Decimal('-Infinity')
		bestMove = 15
		for moves in range (0,len(valid)):
			board[valid[moves]-1]=player
			val = minamax(board, depth-1, not maximizingPlayer, player)
			bestValue = max(bestValue,val)
		return bestValue
	else:
		bestValue = Decimal('Infinity')
		for moves in valid:
			board[valid[moves]-1]=otherPlayer(player)
			val = minamax(board, depth-1, not maximizingPlayer, player)
			bestValue = min(bestValue, val)
			return bestValue
	
def value(board, player):
	score = 0

	score += evaluateLine(player, board, 0, 1, 2)
	score += evaluateLine(player, board, 3, 4, 5)
	score += evaluateLine(player, board, 6, 7, 8)

	score += evaluateLine(player, board, 0, 3, 6)
	score += evaluateLine(player, board, 1, 4, 7)
	score += evaluateLine(player, board, 2, 5, 8)

	score += evaluateLine(player, board, 0, 4, 8)
	score += evaluateLine(player, board, 2, 4, 6)
	return score
	
def evaluateLine(player, board, x, y, z):
	score = 0

	if board[x] == player and board[y] == player and board[z] == player:
		score = 111

	if board[x] == player and board[y] == player and board[z] == EMPTY:
		score = 11
	if board[x] == EMPTY and board[y] == player and board[z] == player:
		score = 11
	if board[x] == player and board[y] == player and board[z] != EMPTY:
		score = 10
	if board[x] != EMPTY and board[y] == player and board[z] == player:
		score = 10

	if board[x] == player and board[y] == EMPTY and board[z] == player:
		score = 2
	if board[x] == player and board[y] != EMPTY and board[z] == player:
		score = 1

	if board[x] == player and board[y] == EMPTY and board[z] == EMPTY:
		score = 1
	if board[x] == EMPTY and board[y] == player and board[z] == EMPTY:
		score = 1
	if board[x] == EMPTY and board[y] == EMPTY and board[z] == player:
		score = 1

	if board[x] == EMPTY and board[y] == EMPTY and board[z] == EMPTY:
		score = 0

	if board[x] == player and board[y] != EMPTY and board[z] != EMPTY:
		score = -10
	if board[x] != EMPTY and board[y] == player and board[z] != EMPTY:
		score = -10
	if board[x] != EMPTY and board[y] != EMPTY and board[z] == player:
		score = -10

	if board[x] != EMPTY and board[y] == player and board[z] != EMPTY:
		score = -1
	if board[x] != EMPTY and board[y] == EMPTY and board[z] != EMPTY:
		score = -2

	if board[x] != EMPTY and board[y] != EMPTY and board[z] == player:
		score = -10
	if board[x] == player and board[y] != EMPTY and board[z] != EMPTY:
		score = -10
	if board[x] != EMPTY and board[y] != EMPTY and board[z] == EMPTY:
		score = -11
	if board[x] == EMPTY and board[y] != EMPTY and board[z] != EMPTY:
		score = -11

	if board[x] != EMPTY and board[y] != EMPTY and board[z] != EMPTY:
		score = -111
	return score	
def otherPlayer(player):
	if player == X:
		return O
	else:
		return X





main()
