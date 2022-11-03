from multiprocessing.resource_sharer import stop
import random

def snake_game(computer,user):
    if computer==user:
        return None
    elif computer=="s":
        if user=="w":
            return False
        elif user=="g":
            return True
    elif computer=="w":
        if user=="s":
            return True
        elif user=="g":
            return False
    elif computer=="g":
        if user=="w":
            return True
        elif user=="s":
            return False
    # elif computer=="s":
    #     if user=="g":
    #         return True
    #     elif user=="w":
    #         return True
    # elif computer=="w":
    #     if user=="g":
    #         return False
    #     elif user=="s":
    #         return True

            
print("Computer Chooses Snake (s) Water (w) and Gun (g)")
computer_turn=random.randint(1,3)
if computer_turn==1:
    computer="s"
elif computer_turn==2:
    computer="w"
elif computer_turn==3:
    computer="g"

user=input("Your Turn Snake (s) Water (w) and Gun (g): ")
    
game=snake_game(computer,user)

print(f'Computer chooses : {computer}')
print(f'And you chooses : {user}')

if game==None:
    print("Game Tie")
elif game==True:
    print("You win the game")
elif game==False:
    print("You loose the game")