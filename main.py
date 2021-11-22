# Program vyhodnotí tip uživatele
# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). 
# Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
import random as r
ODDELOVAC = 40 * "-"
flag = False
print('Hi there!')
print(ODDELOVAC)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(ODDELOVAC)
generate_num = r.sample(range(1000,9999),1)
secret_num = int("".join(map(str,generate_num)))
try:
    while True:
        player_guess = input('ENTER A NUMBER: ')
        if len(player_guess) > 4 or len(player_guess) < 4 or player_guess[0] == '0' or len(set(player_guess)) != len(player_guess):
            print('Wrong input. Guesswork must contains precisely 4 numbers, must not start with 0 and every number must be unique.')
            exit()
except ValueError:
    print('Wrong input. Guesswork must cointains only numbers.')
