import random
import time
from ig_list import *
from replit import clear
from art import *

def user_choice(choice, rank, to_compare):
    global current_score
    global refresh
    #Correct choice
    if choice == 'higher' and to_compare['followers'] > rank['followers']:
        current_score += 1
        return False
    elif choice == 'lower' and to_compare['followers'] < rank['followers']:
        current_score += 1
        return False
    #Wrong choice
    elif choice == 'higher' and to_compare['followers'] < rank['followers']:
        print(f"\nOof. \33[34m{to_compare['owner']}\33[0m actually has \33[1;33m{to_compare['followers']} million\33[0m followers.")
        input("\n\33[31m[Hit Enter]\33[0m")
        refresh()
        print(f"Your final score: \33[1;4;31m{current_score}\33[0m\n")
        print("Hurry! Play again to hide that awful score!")
        return True
    elif choice == 'lower' and to_compare['followers'] > rank['followers']:
        print(f"\nOof. \33[34m{to_compare['owner']}\33[0m actually has \33[1;33m{to_compare['followers']} million\33[0m followers.")
        input("\n\33[31m[Hit Enter]\33[0m")
        refresh()
        print(f"Your final score: \33[1;4;31m{current_score}\33[0m\n")
        print("Hurry! Play again to hide that awful score!")
        return True

def comparing():
    rank = random.choice(ig_list)
    print(f"""\33[4;34m{rank['username']}\33[0m 
Owned by \33[34m{rank['owner']}\33[0m 
\33[1;33m{rank['followers']} million\33[0m followers""") 
    for i in range(len(ig_list)):
        if ig_list[i]['username'] == rank['username']:
            del ig_list[i]
            break
    time.sleep(1)
    vs()
    time.sleep(1)
    to_compare = random.choice(ig_list)
    print(f"""\33[4;34m{to_compare['username']}\33[0m 
Owned by \33[34m{to_compare['owner']}\33[0m""")
    return rank, to_compare

def loading(a):
    if a == "Start":
        b = "2"
    elif a == "Exit":
        b = "1"
    clear()
    logo()
    slogan()
    print(f"\33[3{b}m{a}ing game.\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    slogan()
    print(f"\33[3{b}m{a}ing game..\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    slogan()
    print(f"\33[3{b}m{a}ing game...\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    slogan()

def refresh():
    clear()
    logo()
    slogan()
    
####----------####
should_end = False
while not should_end:
    current_score = 0
    loading("Start")   

    end_game = False
    while not end_game:
        refresh()
        print(f"High score = \33[1;31m{current_score}\33[0m\n")
        time.sleep(1)
        
        rank, to_compare = comparing()

        time.sleep(1)
        choice = input("\nHigher or Lower?\n").lower()
        end_game = user_choice(choice, rank, to_compare)

    invalid_input = True
    while invalid_input == True:
        time.sleep(1)
        cont = input("\33[32mY\33[0m/\33[31mN\33[0m\n").lower()
        if cont == 'n':
            should_end = True
            invalid_input = False
            loading("Exit")
        elif cont == 'y':
            invalid_input = False
            continue
        else:
            clear()
            print('[Invalid input]')