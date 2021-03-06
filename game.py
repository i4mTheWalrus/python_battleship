import board
from random import randint

def main():
    BOARD_SIZE = 5

    # Setup player board
    print("\n\n\n\nWelcome to Batttleship!\n")
    player_board = board.Battleship_Board(BOARD_SIZE)
    player_board.print_board()
    print("\nPlease place your ship. Choose a row and column. (1-5)")
    # force user into loop if ship chosen is out of bounds
    valid_board = False
    while not valid_board:
        print("row:", end = " ")
        chosen_row = int(input())
        print("col:", end = " ")
        chosen_col = int(input())
        valid_board = player_board.place_ship(chosen_row, chosen_col)
        if not valid_board:
            print("row or column chosen is out of bounds")
    print("\nNice! Here's your board:\n")
    player_board.print_board()

    # Setup computer board
    print("\nGenerating the computer's board...")
    computer_board = board.Battleship_Board(BOARD_SIZE)
    computer_board.place_ship_rand()

    # Begin the game!
    game_over = False
    turn = 0
    print("Let the game begin!\n")
    while not game_over:
        print("Press Enter to start next turn...")
        input()
        turn += 1
        print("\n\n----------------------------\n\n")
        print("Turn " + str(turn))
        
        # player goes first
        print("\nYour opponents board:\n")
        computer_board.print_board_hidden()
        # take input to fire at opponent board
        print("\nFire your cannon!!!")
        print("row:", end = " ")
        row = int(input())
        print("col:", end = " ")
        col = int(input())

        if computer_board.receive_shot(row, col):
            # your shot hit!
            computer_board.print_board()
            print("You hit the opponents ship! You win!")
            game_over = True
            continue
        else:
            print ("Your shot missed!! Press Enter for opponents turn...")
            input()

        # opponents turn
        rand_row = randint(0, BOARD_SIZE - 1)
        rand_col = randint(0, BOARD_SIZE - 1)
        while not player_board.computer_shot_valid(rand_row, rand_col):
            rand_row = randint(0, BOARD_SIZE)
            rand_col = randint(0, BOARD_SIZE)
        print("\nComputer chose row %d column %d." %(rand_row, rand_col))
        if player_board.receive_shot(rand_row, rand_col):
            # opponent hit your ship!
            player_board.print_board()
            print("Your opponent hit your ship! You lose!")
            game_over = True
            continue
        else:
            print("Your board after opponents shot:\n")
            player_board.print_board()


    else:
        print("\nThanks for playing!\n")

if __name__ == "__main__":
    main()
