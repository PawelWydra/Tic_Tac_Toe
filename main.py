import random

### START ###

should_continue = True
print("Welcome in TIC TAC TOE Game \n")

###lists for save position ###

player_position = []
cmp_position = []
free_position = [i for i in range(0, 9)]

### Creating variables for game board ###

position = []
for i in range(0, 9):
    position.append(" ")

### lists of all winning combination ###

winning_positions = [["0", "1", "2"],
                     ["3", "4", "5"],
                     ["6", "7", "8"],
                     ["0", "3", "6"],
                     ["1", "4", "7"],
                     ["2", "5", "8"],
                     ["0", "4", "8"],
                     ["2", "4", "6"]]


game_board = (f" {position[0]}|{position[1]}|{position[2]}\n"
              "-------\n"
              f" {position[3]}|{position[4]}|{position[5]}\n"
              "-------\n"
              f" {position[6]}|{position[7]}|{position[8]}\n")
print(game_board)

while should_continue:
    ### PLAYER LOGIC ###

    player_move = input(f"Choose your position from {free_position}")
    player_position.append(player_move)
    position[int(player_move)] = "X"
    free_position.remove(int(player_move))

    ### COMPUTER LOGIC ###

    cmp_move = random.choice(free_position)
    cmp_position.append(str(cmp_move))
    position[cmp_move] = "O"
    free_position.remove(cmp_move)

    ### PRINT GAME BOARD ###

    game_board = (f" {position[0]}|{position[1]}|{position[2]}\n"
                  "-------\n"
                  f" {position[3]}|{position[4]}|{position[5]}\n"
                  "-------\n"
                  f" {position[6]}|{position[7]}|{position[8]}\n")
    print(game_board)

    ### CHECK WINNING ###

    for x in winning_positions:
        if x[0] in player_position:
            if x[1] in player_position:
                if x[2] in player_position:
                    play_again = input("You win, wanna play again? Yes/No?").title()
                    if play_again == 'No':
                        should_continue = False

        elif x[0] in player_position:
            if x[1] in player_position:
                if x[2] in player_position:
                    play_again = input("Computer win, wanna play again? Yes/No?").title()
                    if play_again == 'No':
                        should_continue = False
