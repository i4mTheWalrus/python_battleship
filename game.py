import board
from random import randint

def main():
	BOARD_SIZE = 5

	# Setup player board
	print "Welcome to Batttleship!"
	player_board = board.Battleship_Board(BOARD_SIZE)
	print "Please place your ship. Choose a row and column. (1-5)"
	# force user into loop if ship chosen is out of bounds
	valid_board = False
	while not valid_board:
		chosen_row = int(raw_input("row: "))
		chosen_col = int(raw_input("col: "))
		valid_board = player_board.place_ship(chosen_row, chosen_col)
		if not valid_board:
			print "row or column chosen is out of bounds"
	print "\nNice! Here's your board:"
	player_board.print_board()

	# Setup computer board
	print "\nGenerating the computer's board"
	computer_board = board.Battleship_Board(BOARD_SIZE)
	computer_board.place_ship_rand()

	# Begin the game!
	game_over = False
	turn = 0
	while not game_over:
		turn += 1
		print "\nTurn " + str(turn)
		
		# player goes first
		print "Your opponents board:"
		computer_board.print_board_hidden()
		# take input to fire at opponent board
		print "Fire your cannon!!!"
		row = int(raw_input("row: "))
		col = int(raw_input("col: "))

		if computer_board.receive_shot(row, col):
			# your shot hit!
			computer_board.print_board()
			print "You hit the opponents ship! You win!"
			game_over = True
			continue
		else:
			print "Your shot missed!"

		# opponents turn
		rand_row = randint(0, BOARD_SIZE - 1)
		rand_col = randint(0, BOARD_SIZE - 1)
		while not player_board.computer_shot_valid(rand_row, rand_col):
			rand_row = randint(0, BOARD_SIZE - 1)
			rand_col = randint(0, BOARD_SIZE - 1)
		print "\nComputer chose row %d column %d." %(rand_row, rand_col)
		if player_board.receive_shot(rand_row, rand_col):
			# opponent hit your ship!
			player_board.print_board()
			print "Your opponent hit your ship! You lose!"
			game_over = True
			continue
		else:
			print "Your board after opponents shot:"
			player_board.print_board()


	else:
		print "Thanks for playing!"

if __name__ == "__main__":
	main()
