from adventurelib import *

# import random

# riddle = {
#     'r_a' : {
#         'question': 'What has to be broken before you can use it?',
#         'answer':'egg'
#     },
#     'r_b' : {
#         'question': 'I am tall when I am young, and I am short when I \
#            am old. What am I?',
#         'answer': 'candle'
#     },
#     'r_c' : {
#         'question': 'What month of the year has 28 days?',
#         'answer': 'all'
#     },
#     'r_d' : {
#         'question': 'What is full of holes but still holds water?',
#         'answer': 'sponge'
#     },
#     'r_e' : {
#         'question': 'What is always in front of you but can’t be seen?',
#         'answer': 'future'
#     },
#     'r_f' : {
#         'question': 'What gets wet while drying?',
#         'answer': 'towel'
#     },
#     'r_g' : {
#         'question': 'I shave every day, but my beard stays the same. What am I?',
#         'answer': 'barber'
#     },
#     'r_h' : {
#         'question': 'What can’t talk but will reply when spoken to?',
#         'answer': 'echo'
#     },
#     'r_i' : {
#         'question': 'The more of this there is, the less you see. What is it?',
#         'answer': 'darkness'
#     },
#     'r_j' : {
#         'question': 'What goes up and down but doesn’t move?',
#         'answer': 'staircase'
#     }
# }


def ear_plugs(inventory, player_answer):
    """
    Player can choose to pick the object 'earplugs' and store it
    in the inventory.
    Requests yes/no answer from player to keep playing.
    Updates the inventory dictionary to True when object is picked.
    """
    if player_answer == 'yes':
        print(f"\nThe earplugs are now in your pocket.\n")
        inventory["earplugs"] = True
        return True
    elif player_answer == 'no':
        return False
    else:
        player_answer = input(f"\nInvalid answer, please type 'yes' or\
        'no' only.\n").lower()
        ear_plugs(inventory, player_answer)


def door_choice(inventory):
    """
    Player can choose to go through red or blue door.
    Requests correct answer from player to keep playing.
    """
    door_answer = input(f"\nThere are two doors in front of you, one is red,\
    the other one is blue. You need to choose one, type 'red' or\
        'blue'.\n").lower()

    if door_answer == 'blue':
        print("\nThere is a hangry wolf in the room, the door has locked at\
        your back. You die!\n")
        game_over()
    if door_answer == 'red':
        firebird_room(inventory)
    if door_answer != 'blue' or 'red':
        print(f"\nInvalid answer, please type 'red' or 'blue' only.\n")
        door_choice(inventory)


def firebird_room(inventory):
    """
    Player needs to solve the Firebird's riddle
    """
    a = (f" 2: In the next room you find a majestuous Firebird at the central\
    area, blocking your way to the next door. You try to reach the exit very\
    carefully trying not to disturb the bird but she wakes up and open \
    her wings. She looks right into your eyes and telepathically tells you \
    that if you wishto go through the door you will need to solve the \
    following riddle:\n")

    print(a)

    # f_riddle = random.choice(list(riddle.keys()))
    # print(f_riddle)
    riddle = input(f"What belongs to you but is used by everyone?\n").lower()

    if riddle == "your name" or riddle == "name":
        print("\nWell done! The Firebird gifts you with a key.\n")
        mermaid_room(inventory)
        inventory["exit_key"] = True
        game_win()
        exit()
        return True

    else:
        riddle = input(f"Incorrect answer, try again!\n").lower
        firebird_room(inventory)


def mermaid_room(inventory):
    """
    Level 3 of the game. Function access game_over() and the inventory
    dictionary.
    """
    print(f"\nLevel 3: A mermaid is singing beautifully in the room. the next\
    door is easily accessible.\n")
    mermaid_choice = input(f"\nDo you want to listen to her or use\
    the earplugs? Type 'listen' or 'earplugs'\n").lower()

    if mermaid_choice == 'listen':
        print(f"\nYou got enchanted and stay listening to the mermaid\
        forever. You die!\n")
        game_over()
    elif mermaid_choice == 'earplugs':
        x = inventory.get('earplugs')
        if x is True:
            sorcerer_room(inventory)
        else:
            print(f"\nYou didn't pick the earplugs before and now\
            you got enchanted by the mermaid. You die!\n")
            game_over()
    else:
        print("\nIncorrect answer, type 'listen' or 'earplugs' only.\n")
        mermaid_room(inventory)


def sorcerer_room(inventory):
    """
    Level 4 of the game. Relates to previous function mermaid_room() and next
    function garden_room().
    """
    print(f"\nLevel 4: A sorcerer is standing in front of you, you will pass if\
        you solve the riddle.\n")
    sorcerer_riddle = input(f"\nIt is beautiful, colorful and magical.\
        It lives up in the sky but can't fly. What is it?\n").lower()

    if sorcerer_riddle == 'rainbow':
        garden_room(inventory)
    else:
        print("\nIncorrect answer, try again!\n")
        sorcerer_room(inventory)


def garden_room(inventory):
    """
    Level 5 of the game.
    """
    print("\nLevel 5: You managed to get outside of the building, it seems \
    you are in a garden in front of a fence with 2 doors.\n")
    garden_choice = input("\nWhich one will you take, the green or the yellow \
    door? Type 'green' or 'yellow'\n").lower()

    if garden_choice == 'yellow':
        y = inventory.get('exit_key')
        if y is True:
            game_win()
    elif garden_choice == 'green':
        print("\nEverything is very dark and you don't see the cliff. \
        You die!\n")
        game_over()
    else:
        print("\nIncorrect answer, type 'green' or ''yellow' only.\n")
        garden_room(inventory)


def game_win():
    print('\nYOU GOT OUT OF THE MISTERY HOUSE, YOU WON!\n')
    game_replay()


def game_over():
    """
    Ends the game and asks the player if s/he wants to play again
    """
    print('GAME OVER')
    game_replay()


def game_replay():
    """
    docstring
    """
    replay = input(f"\nDo you want to play again? yes/no\n").lower()
    if replay == 'yes':
        main()
    elif replay == 'no':
        print(f"\nThank you for playing with us. Hope to see you soon!\n")
        exit()
    else:
        print("\nPlease type 'yes' or 'no' only. Do you want to play again?\n")
        game_replay()


def main():
    """
    Calls all the functions in the game
    """
    print("\nWelcome to Adventureland, the adventure of your life!\n")

    player_name = input(F"\nPlease enter your name: \n")

    s = (f"Room 1: Hello {player_name}, you just wake up and do not recognise \
        the room around you. The last thing your remember is that you were \
        going back home after spending the afternoon with your friends on \
        the street and one of a sudden everything turned blurry. The room \
        is completely empty except for some earplugs in one corner.\n")

    print(s)

    player_answer = input(f"\nDo you want to pick up the earplugs? \
    yes/no\n").lower()

    inventory = {
        "earplugs": False,
        "exit_key": False
        }

    ear_plugs(inventory, player_answer)
    door_choice(inventory)


if __name__ == '__main__':
    main()
