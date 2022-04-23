from random import randint

class Battleship_Board:

	def __init__(self, size):
		# create a 5x5 board filled with string O for Ocean
		self.board = []
		self.board_size = size
		for i in range(self.board_size):
			self.board.append(["O"] * self.board_size)
	
	def check_range(self, num):
		# check that a number is within the board
		if num <= self.board_size and num > 0:
			return True
		else:
			return False

	def computer_shot_valid(self, row, col):
		# used to ensure the computer doesn't choose a spot on
		# the board that they have already chosen
		if self.check_range(row) and self.check_range(col):
			if self.board[row - 1][col - 1] == "X":
				return False
			else:
				# space is either "O" or "S"
				return True
		else:
			return False
		

	def print_board(self):
		# print the status of the board to the console
		for row in self.board:
			print(" ".join(row))

	def print_board_hidden(self):
		# prints the status of the board to the console, and hides the ship
		for row in self.board:
			new_row = []
			for i in row:
				if i == "S":
					new_row.append("O")
				else:
					new_row.append(i)
			print(" ".join(new_row))

	def place_ship_rand(self):
		# place ship on board, represented by S
		rand_row = randint(0, self.board_size - 1)
		rand_col = randint(0, self.board_size - 1)
		self.board[rand_row][rand_col] = "S"

	def place_ship(self, row, col):
		# place ship in a specified location
		# row, col are not index values
		if self.check_range(row) and self.check_range(col):
			self.board[row - 1][col - 1] = "S"
			return True
		else:
			return False
	
	def receive_shot(self, row, col):
		# intake a row and col, to see if the ship is found
		# if not, replace with x
		if self.check_range(row) and self.check_range(col):
			# shot is in board
			row -= 1
			col -= 1
			if self.board[row][col] == "S":
				# ship has been hit
				self.board[row][col] = "!"
				return True
			else:
				self.board[row][col] = "X"
				return False
		else:
			return False
