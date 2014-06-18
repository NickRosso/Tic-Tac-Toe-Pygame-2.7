import pygame
from pygame.locals import *
import random
import time


pygame.init()
DISPLAY = pygame.display.set_mode((300,300),0,32)
pygame.display.set_caption('Tic Tac Toe')

BLACK =   0,  0,  0
TEAL =  193, 254, 212
running = True


X = "X"
O = "O"
won = False

turn = random.choice((X,O))

Ximg = pygame.image.load("X.png")
Oimg = pygame.image.load("O.png")




coords = [(0,0),(100,0),(200,0),
		 (0,100),(100,100),(200,100),
		 (0,200),(100,200),(200,200)]


board = [None,None,None,
		 None,None,None,
		 None,None,None]
print "Hit Spacebar to reset board"

def template():
	pygame.draw.line(DISPLAY, BLACK, (100, 0),(100, 300), 2)
	pygame.draw.line(DISPLAY, BLACK, (200, 0),(200, 300), 2)
	pygame.draw.line(DISPLAY, BLACK, (0, 100),(300, 100), 2)
	pygame.draw.line(DISPLAY, BLACK, (0, 200),(300, 200), 2)

	for n in range(0,9):
		if board[n] == X:
			DISPLAY.blit(Ximg, (coords[n]))

		if board[n] == O:
			DISPLAY.blit(Oimg, (coords[n]))
			
		
	
	


def drawXO(row, col):
	
	
	if row == 1 and col == 1 and  board[0] == None:
		board[0] = turn

	if row == 2 and col == 1 and board[1] == None:
		board[1] = turn
		
	if row == 3 and col == 1 and board[2] == None:
		board[2] = turn
		


	if row == 1 and col == 2 and board[3] == None:
		board[3] = turn
		
	if row == 2 and col == 2 and board[4] == None:
		board[4] = turn
		
	if row == 3 and col == 2 and board[5] == None:
		board[5] = turn
		
		


	if row == 1 and col == 3 and board[6] == None:
		board[6] = turn
		
	if row == 2 and col == 3 and board[7] == None:
		board[7] = turn
		
	if row == 3 and col == 3 and board[8] == None:
		board[8] = turn
	



def isWin():
	#checks horizontal wins and vertical wins
	if isRowWin(board[0], board[1], board[2]) or isRowWin(board[0], board[3], board[6]):
		printWinner(board[0])
		print "1"
		
	if isRowWin(board[3], board[4], board[5]):
		printWinner(board[3])
		print "2"

	if isRowWin(board[1], board[4], board[7]):
		printWinner(board[1])
		
	if isRowWin(board[6], board[7], board[8]) or isRowWin(board[2], board[5], board[8]):
		printWinner(board[6])
		print "3"
	#check diagonal win	
	if isRowWin(board[0], board[4], board[8]):
		printWinner(board[0])
		
	if isRowWin(board[2], board[4], board[6]):
		printWinner(board[2])
		
	if isTie() == True:
		printWinner(None)	
	
	
def isRowWin(one, two, three):
	return one != None and one == two == three
	

def printWinner(XO):
	print "The winner is %s" % XO

def isTie():
	if None in board:
		return False
	else:
		return True

def mouse_clicked():
	
	row, col = pygame.mouse.get_pos()

	if col < 100:
		col = 1

	if col >= 100 and col < 200:
		col = 2

	if col > 200 and col <= 300:
		col =  3

	if row < 100:
		row =  1

	if row >= 100 and row <200:
		row = 2

	if row > 200 and col <= 300:
		row = 3
	
	drawXO(row, col)
	isWin()


def turns(current_turn):

	if turn == X:
		current_turn = O
		return current_turn
		
	if turn == O:
		current_turn = X
		return current_turn
		
	
while running:
	
	DISPLAY.fill(TEAL)
	template()
	
	key = pygame.key.get_pressed()

	if key[pygame.K_SPACE]:

		board = [None,None,None,
		 		 None,None,None,
				 None,None,None]

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		

		elif event.type == MOUSEBUTTONDOWN:
			
			mouse_clicked()
			turn = turns(turn)
			


	pygame.display.update()
