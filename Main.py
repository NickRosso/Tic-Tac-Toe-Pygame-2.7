import random
from GUI import *

def draw_XO(row, col, board, turn):
	if is_cell_taken(row, col, 1, 1, board[0]):
		board[0] = turn
		
	if is_cell_taken(row, col, 2, 1, board[1]):
		board[1] = turn

	if is_cell_taken(row, col, 3, 1, board[2]):
		board[2] = turn

	if is_cell_taken(row, col, 1, 2, board[3]):
		board[3] = turn
	
	if is_cell_taken(row, col, 2, 2, board[4]):
		board[4] = turn

	if is_cell_taken(row, col, 3, 2, board[5]):
		board[5] = turn
	
	if is_cell_taken(row, col, 1, 3, board[6]):
		board[6] = turn
		
	if is_cell_taken(row, col, 2, 3, board[7]):
		board[7] = turn

	if is_cell_taken(row, col, 3, 3, board[8]):
		board[8] = turn
	
def is_cell_taken(row, col, x, y, content):
	return row == x and col == y and content == None

	
def is_win(board):
	if is_row_win(board[0], board[1], board[2]) or is_row_win(board[0], board[3], board[6]):
		print_winner(board[0])
		
	if is_row_win(board[3], board[4], board[5]):
		print_winner(board[3])
		
	if is_row_win(board[1], board[4], board[7]):
		print_winner(board[1])
		
	if is_row_win(board[6], board[7], board[8]) or is_row_win(board[2], board[5], board[8]):
		print_winner(board[6])
		
	if is_row_win(board[0], board[4], board[8]):
		print_winner(board[0])
		
	if is_row_win(board[2], board[4], board[6]):
		print_winner(board[2])
		
	if is_tie(board) == True:
		print_winner(None)	
	
def is_row_win(row_start, row_middle, row_end):
	return row_start != None and row_start == row_middle == row_end
	
def print_winner(XO):
	print "The winner is %s" % XO
	print "-------------Press Space For New Game------------------"

def is_tie(board):
	if None in board:
		return False
	else:
		return True

def mouse_clicked(board, turn):
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
	
	draw_XO(row, col, board, turn)
	is_win(board)

def turns(turn):
	if turn == X:
		current_turn = O
		return current_turn
		
	if turn == O:
		current_turn = X
		return current_turn

def main():		
	pygame.init()
	DISPLAY = pygame.display.set_mode((300,300))
	pygame.display.set_caption('Tic Tac Toe')
	clock = pygame.time.Clock()
	fps = 30

	running = True
	won = False
	turn = random.choice((X,O))

	coords = [(0,  0),(100,  0),(200,  0),
		 	  (0,100),(100,100),(200,100),
		      (0,200),(100,200),(200,200)]

	board = [None]*9

	while running:
		template(DISPLAY, board, Ximg, Oimg, coords)
		
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:

			board = [None]*9

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == MOUSEBUTTONDOWN:
				
				mouse_clicked(board, turn)
				turn = turns(turn)

		pygame.display.update()
		clock.tick(fps)
	pygame.quit()

if __name__ == "__main__":
	main()
