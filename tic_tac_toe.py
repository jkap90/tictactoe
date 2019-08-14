'''
Tic Tac Toe
'''
import random

print('Welcome to Tic Tac Toe!')


board = [' #', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ']
test_board = [' #', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ']
def display_board(board):
	print(board[7] + '|' + board[8] + '|' + board[9])
	print(board[4] + '|' + board[5] + '|' + board[6])
	print(board[1] + '|' + board[2] + '|' + board[3])

'''
The output of player_input() is in the form of a tuple, (player 1 marker, player 2 marker)
'''

def player_input():
	marker = ''
	
	'''
	Basically, this loop says:
		while the variable (marker) is not = to anything, or, in this case, not equal to X or O,
		keep displaying this question input("Player 1, please pick marker: 'X' or 'O'").upper()
	'''
	while marker != 'x' and marker != 'o':
		#this next line  has .upper() attached to the end so it doesn't matter if the user enters a lowercase letter
		marker = input("Player 1, please pick marker: 'X' or 'O'").upper()
		if marker == 'X':
			return ('X', 'O')
		else:
			return('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker

def check_win(board, marker):
	win = False
	# Horizontal Win Conditions
	if board[1] == board[2] == board[3] == marker:
		win = True
	elif board[4] == board[5] == board[6] == marker:
		win = True
	elif board[7] == board[8] == board[9] == marker:
		win = True
	# Vertical Win Conditions
	elif board[1] == board[4] == board[7] == marker:
		win = True
	elif board[2] == board[5] == board[8] == marker:
		win = True
	elif board[3] == board[6] == board[9] == marker:
		win = True
	# Diagaonal Win Conditions
	if board[1] == board[5] == board[9] == marker:
		win = True
	elif board[3] == board[5] == board[7] == marker:
		win = True
	else:
		pass
	
	# if win is true
	if win:
		print("Player has won the game!")
	else:
		pass
def choose_first():
	
		'''
		Chooses whose turn it is to go first


		This calls the random module we imported
		and uses the random integer method.
		it chooses a random integer from the integers provided.
		'''
		flip = random.randint(0,1)

		if flip == 0:
			return 'Player 1'
		else:
			return 'Player 2'
def space_check(board, position):
		# checks to see if board space is empty
		board[position] == ' '
def full_board_check(board):
		'''
		There are 9 spaces but we start counting at position 0
		so we start at 1 and count to 10

		we call the space check function

		'''
		for i in range(1,10):
			if space_check(board, i):
				return False
		# Board is full if return True
		return True
def player_choice(board):

		position = 0

		while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
			position = int(input('Choose a position: (1-9)'))
def replay():
		choice = input('Play again? Y or N ?').upper()

		return choice == 'Y'


while True:
	#play the game

	#set everything up
	# = ['', '', '', '', '', '', '', '', '', '']
	game_board = [''] *10
	player1_marker, player2_marker = player_input()

	turn = choose_first()
	print(turn + ' goes first.')

	play_game = input('Ready to play? Y or N?').upper
	if play_game == 'Y':
		game_state = True
	else:
		game_state = False
	#gameplay
	while game_board:
		if turn == 'Player 1':
			#display board
			display_board(game_board)

			#choose position
			position = player_choice(game_board)
		
			# Place marker on position
			place_marker(game_board, player1_marker, position)
			display_board(game_board)
			# check if they won
			if check_win(game_board, player1_marker):
				display_board(game_board)
				print('Player 1 has won the game.')
				game_state = False
			# check for tie
			else:
				# check to see whether or not the game board is full
				if full_board_check(game_board):
					print('The board is full. There is no winner.')
					game_state = False
				else:
					turn = 'Player 2'
			

			#no tie or win? next player's turn
	##Player 1 turn

	##PLayer 2 turn

		else: 
			turn == 'Player 2'
			#display board
			display_board(game_board)

			#choose position
			position = player_choice(game_board)
					
			# Place marker on position
			place_marker(game_board, player2_marker, position)
			display_board(game_board)
			# check if they won
			if check_win(game_board, player2_marker):
				display_board(game_board)
				print('Player 2 has won the game.')
				game_state = False
			# check for tie
			else:
				# check to see whether or not the game board is full
				if full_board_check(game_board):
					print('The board is full. There is no winner.')
					game_state = False
				else:
					turn = 'Player 1'
	if not replay():
		break


