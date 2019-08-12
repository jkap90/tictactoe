'''
Tic Tac Toe
'''


def start_game():
	board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ']

	def display_board():
		print(board[7] + '|' + board[8] + '|' + board[9])
		print(board[4] + '|' + board[5] + '|' + board[6])
		print(board[1] + '|' + board[2] + '|' + board[3])

	marker1= ''
	marker2= ''
	player1 = input("Please pick marker: 'X' or 'O'")
	if 'x':
		marker1 = 'X'
		marker2 = '0'
		print("'Player 1 has chosen 'X', Player 2 will be 'O'")
	elif 'o':
		marker1 = 'O'
		marker2 = 'X'
		print("'Player 1 has chosen 'O', Player 2 will be 'X'")
	
	display_board()
	
	def check_win():
		win = False

		# Horizontal Win Conditions
		if board[1] == board[2] == board[3]:
			win = True
		elif board[4] == board[5] == board[6]:
			win = True
		elif board[7] == board[8] == board[9]:
			win = True

		# Vertical Win Conditions
		elif board[1] == board[4] == board[7]:
			win = True
		elif board[2] == board[5] == board[8]:
			win = True
		elif board[3] == board[6] == board[9]:
			win = True

		# Diagaonal Win Conditions
		if board[1] == board[5] == board[6]:
			win = True
		elif board[3] == board[5] == board[7]:
			win = True
		else:
			pass
		
		if win = True:
			pass #print(f"Player {} has won the game!")
		else:
			pass


	def player1_turn():
		pass
	def player2_turn():
		pass
		
	def choose_space():
		space = input('Using your num pad, where would you like to place your marker?')
		if space == '1':
			board[1] = marker1
		elif space == '2':
			board[2] = marker1
		elif space == '3':
			board[3] = marker1
		elif space == '4':
			board[4] = marker1
		elif space == '5':
			board[5] = marker1
		elif space == '6':
			board[6] = marker1
		elif space == '7':
			board[7] = marker1
		elif space == '8':
			board[8] = marker1
		elif space == '9':
			board[9] = marker1
		else:
			pass
		display_board()
	
	choose_space()

	


start_game()