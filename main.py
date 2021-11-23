import random as r
import datetime

SEPARATOR = 40 * "-"

print('Hi there!')
print(SEPARATOR)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(SEPARATOR)

# Vygenerování náhodného čísla. Pokud je v listu, kde jsou číla uložená duplicita generuje se stále nový list dokud nejsou všechny čísla unikátní
while True:
    secret_num = r.sample(range(1, 9),4)
    if len(set(secret_num)) != len(secret_num):
        continue
    else:
        break

# Funkce, která řeší průběh celé hry, 
def play_game(secret_num):
    # Smyčka, která se ukončí až když hráč uhodne číslo 
    try:
        attempts = 0
        while True:
            bulls = 0
            cows = 0
            save_guess = []
            attempts +=1
            # Pokud hráč nesplní podmínky pro správný vstup je upzorněn a vyzván pro opětovný vstup dokud vstup není správný
            while True:
                player_guess = input('ENTER FOUR NUMBERS: ')
                if len(player_guess) > 4 or len(player_guess) < 4 or player_guess[0] == '0' or len(set(player_guess)) != len(player_guess):
                    print('Wrong input. Your guess must cointains precisely 4 numbers, must not start with 0 and every number must be unique.')
                    print(SEPARATOR)  
                else:
                    break
            # Smyčka která uloží jednotlivá čísla z inputu do listu a změný datový typ na int
            for i in range(4):
                save_guess.append(int(player_guess[i]))
            # Smyčka která kontroluje zda jsou nějaký čísla, které hráč háda na správném indexu nebo zda se aspoň nachází v hádaném čísle
            # Pokud ano, tak se do proměnné bulls a cows přičte jedna za každý výskyt dle pravidel hry
            for i,num in enumerate(save_guess):
                    if save_guess[i] == secret_num[i]:
                        bulls += 1
                    if num in secret_num and not save_guess[i] == secret_num[i]:
                        cows += 1 
            if bulls == 1 or bulls == 0:
                bull_str = 'bull'
            else:
                bull_str = 'bulls'
            if cows == 1 or cows == 0:
                cows_str = 'cow'
            else:
                cows_str = 'cows'
            print(f'{bulls} {bull_str}, {cows} {cows_str}')
            print(SEPARATOR)
            # Pokud se proměnná bulls rovná čtyřem znamená to, že hráč uhádl hádané číslo
            # do souboru Statistics.txt uložíme aktuální datum a čas s počtem pokusů za každou odehranou hru
            # po uložení program vrátí False a tím se celá while smyčka ve které hra běží ukončí
            if bulls == 4:
                print(f"Correct, you've guessed the right number in {attempts} guesses!")
                 if attempts < 3:
                    print('Amazing result! :)')
                elif attempts > 3 and attempts < 8:
                    print('Average result.')
                else:
                    print('That is not good result. :(')
                date = datetime.datetime.now()
                date_edit = date.strftime('%d/%m/%Y %X')
                with open('Statistics.txt', 'a') as sta:
                    sta.write(f'{date_edit} - Number o attempts: {attempts}\n')
                    return False
    except ValueError:
        print('Wrong input. You must type only numbers.') 
        print('EXIT...')
play_game(secret_num)
