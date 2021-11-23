# Program vyhodnotí tip uživatele
# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). 
# Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
import random as r
import time

ODDELOVAC = 40 * "-"

print('Hi there!')
print(ODDELOVAC)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(ODDELOVAC)

while True:
    secret_num = r.sample(range(1, 9),4)
    if len(set(secret_num)) != len(secret_num):
        continue
    else:
        print(secret_num)
        break

def play_game(secret_num):
    attempts = 0
    try:
        while True:
            bulls = 0
            cows = 0
            player_guess = input('ENTER FOUR NUMBERS: ')
            save_guess = []
            attempts +=1
            if len(player_guess) > 4 or len(player_guess) < 4 or player_guess[0] == '0' or len(set(player_guess)) != len(player_guess) or player_guess.isalnum == False:
                print('Wrong input. Guesswork must contains precisely 4 numbers, must not start with 0 and every number must be unique.')
                exit()
            for i in range(4):
                save_guess.append(int(player_guess[i]))
            for i,num in enumerate(save_guess):
                    if save_guess[i] == secret_num[i]:
                        bulls += 1
                    if num in secret_num and not save_guess[i] == secret_num[i]:
                        cows += 1 
            if bulls > 1 or cows > 1:
                print(f'{bulls} Bulls, {cows} Cows')
            elif bulls == 1 or cows == 1:
                print(f'{bulls} Bull, {cows} Cow')
            if bulls == 4:
                print(f"Correct, you've guessed the right number in {attempts} guesses!")
                return False
    except:
        print('Wrong input. Guesswork must cointains only numbers.')

play_game(secret_num)
