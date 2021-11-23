import random as r
import datetime

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
    while True:
        bulls = 0
        cows = 0
        player_guess = input('ENTER FOUR NUMBERS: ')
        print(ODDELOVAC)
        save_guess = []
        attempts +=1
        if len(player_guess) > 4 or len(player_guess) < 4 or player_guess[0] == '0' or len(set(player_guess)) != len(player_guess) or player_guess.isalnum == False:
            print('Wrong input. Your guess must cointains only numbers precisely 4 numbers, must not start with 0, every number must be unique.')
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
            print(ODDELOVAC)
        elif bulls == 1 or cows == 1:
            print(f'{bulls} Bull, {cows} Cow')
            print(ODDELOVAC)
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            date = datetime.datetime.now()
            date_edit = date.strftime('%d/%m/%Y %X')
            with open('Statistics.txt', 'a') as sta:
                sta.write(f'{date_edit} - Number o attempts: {attempts}\n')
                return False

play_game(secret_num)
