import random
from ig_list import *
from replit import clear

def user_choice(choice):
    global current_score
    #Correct choice
    if choice == 'higher' and to_compare['followers'] > rank['followers']:
        current_score += 1
        return False
    elif choice == 'lower' and to_compare['followers'] < rank['followers']:
        current_score += 1
        return False
    #Wrong choice
    elif choice == 'higher' and to_compare['followers'] < rank['followers']:
        print(f"\nOops. {to_compare['owner']} has {to_compare['followers']} million followers.")
        print(f"\nYour score: {current_score}")
        print("You can do better than that.")
        return True
    elif choice == 'lower' and to_compare['followers'] > rank['followers']:
        print(f"\nOops. {to_compare['owner']} has {to_compare['followers']} million followers.")
        print(f"\nYour score: {current_score}")
        print("You can do better than that.")
        return True

current_score = 0

should_end = False
while not should_end:
    end_game = False
    while not end_game:
        clear()
        print(f"High score = {current_score}\n")
        
        rank = random.choice(ig_list)
        print(f"""{rank['username']} 
Owned by {rank['owner']} 
{rank['followers']} million followers""")
        
        for i in range(len(ig_list)):
            if ig_list[i]['username'] == rank['username']:
                del ig_list[i]
                break
    
        print("\nVS.\n")
        
        to_compare = random.choice(ig_list)
        print(f"""{to_compare['username']} 
Owned by {to_compare['owner']}""")
        
        choice = input("\nHigher or Lower?\n[Hint]\n").lower()
        end_game = user_choice(choice)
            
    cont = input("\nRestart game? Y/N ").lower()
    if cont == 'n':
        should_end = True
        print("Exit game")