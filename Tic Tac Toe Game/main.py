# Import Package
import random
# Game Switch
game_is_on = True
# Create A List Can Store The Position
number_list = [i for i in range(1, 10)]
# Create An Empty List Can Fill The O or X
pct_list = [" " for i in range(1, 10)]


# Intro
intro_words = f"Hello!!\n" \
              "Choose O or X being your symbol\n" \
              "Enter number 1 ~ 9.\n" \
              "Position:\n"

number_table = f"  | {number_list[0]} | {number_list[1]} | {number_list[2]} |\n" \
               "  -------------\n" \
               f"  | {number_list[3]} | {number_list[4]} | {number_list[5]} |\n" \
               "  -------------\n" \
               f"  | {number_list[6]} | {number_list[7]} | {number_list[8]} |\n" \
               "  -------------\n"
print(number_table)


# Randomly Choose A Number To Decide Who is First
coin = random.randint(1, 50)


# Who go first ??
def who_go_first(decide):
    if decide % 2 == 1:
        print("Player is first.")
        return True
    else:
        print("Computer is first.")
        return False


# Decide Your Symbol
p_symbol = input("O or X ?? : ")
if p_symbol == "O":
    c_symbol = "X"
else:
    c_symbol = "O"


# Player Input
def p_choose():
    global game_is_on
    # If There Any Space Can Fill , It Will Continue
    if check_empty():
        p_choice = int(input("Choose 1 ~ 9: "))
        while not fill_choice(p_choice, p_symbol):
            print(f"{p_choice} is filled\n"
                  f"Please select another number!")
            p_choice = int(input("Choose 1 ~ 9: "))
    else:
        game_is_on = False


# Computer Input
def c_choose():
    global game_is_on
    if check_empty():
        c_choice = random.randint(1, 9)
        while not fill_choice(c_choice, c_symbol):
            c_choice = random.randint(1, 9)
    else:
        game_is_on = False


# Print Table
def current_table(space):
    begin_table = f"  | {space[0]} | {space[1]} | {space[2]} |\n" \
                  "  -------------\n" \
                  f"  | {space[3]} | {space[4]} | {space[5]} |\n" \
                  "  -------------\n" \
                  f"  | {space[6]} | {space[7]} | {space[8]} |\n" \
                  "  -------------\n"
    print(begin_table + "\n|================|")


# Check is there any % in list
def check_empty():
    if " " in pct_list:
        return True
    else:
        return False


# Fill The choice
def fill_choice(number, symbol):
    if pct_list[number - 1] == " ":
        pct_list[number - 1] = symbol
        return True
    else:
        return False


# Check Player Either Win
def player_is_win():
    if pct_list[0] == pct_list[1] == pct_list[2] == p_symbol:
        return True
    elif pct_list[3] == pct_list[4] == pct_list[5] == p_symbol:
        return True
    elif pct_list[6] == pct_list[7] == pct_list[8] == p_symbol:
        return True
    elif pct_list[0] == pct_list[3] == pct_list[6] == p_symbol:
        return True
    elif pct_list[1] == pct_list[4] == pct_list[7] == p_symbol:
        return True
    elif pct_list[2] == pct_list[5] == pct_list[8] == p_symbol:
        return True
    elif pct_list[0] == pct_list[4] == pct_list[8] == p_symbol:
        return True
    elif pct_list[2] == pct_list[4] == pct_list[6] == p_symbol:
        return True
    else:
        return False


# Check Computer Either Win
def computer_is_win():
    if pct_list[0] == pct_list[1] == pct_list[2] == c_symbol:
        return True
    elif pct_list[3] == pct_list[4] == pct_list[5] == c_symbol:
        return True
    elif pct_list[6] == pct_list[7] == pct_list[8] == c_symbol:
        return True
    elif pct_list[0] == pct_list[3] == pct_list[6] == c_symbol:
        return True
    elif pct_list[1] == pct_list[4] == pct_list[7] == c_symbol:
        return True
    elif pct_list[2] == pct_list[5] == pct_list[8] == c_symbol:
        return True
    elif pct_list[0] == pct_list[4] == pct_list[8] == c_symbol:
        return True
    elif pct_list[2] == pct_list[4] == pct_list[6] == c_symbol:
        return True
    else:
        return False


# Check Who Is Win
def who_is_win():
    if player_is_win() is True and not computer_is_win():
        print("Player is winner.")
        return False
    elif not player_is_win() and computer_is_win() is True:
        print("Computer is winner.")
        return False
    else:
        return True


# Play
def play():
    if who_go_first(coin):
        p_choose()
        c_choose()
        current_table(pct_list)
    else:
        c_choose()
        current_table(pct_list)
        p_choose()


# Play Again
def play_again():
    global game_is_on, pct_list
    error_alert = True
    while error_alert:
        again = input("Will you want to play again? Y/N ").upper()
        if again == "Y":
            game_is_on = True
            error_alert = False
            pct_list = [" " for i in range(1, 10)]
        elif again == "N":
            print("See you again~")
            game_is_on = False
            error_alert = False
        else:
            print("Please Enter Again.")


if __name__ == '__main__':
    while game_is_on:
        play()
        if not who_is_win():
            play_again()
        else:
            if not check_empty():
                print("Draw~")
                play_again()

