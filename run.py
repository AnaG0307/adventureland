print("\nWelcome to Adventureland, the adventure of you life!\n")

player_name = input(F"Pleaser enter your name: \n")


def start_room():
    """
    Explains how to game works, what are the features and gets started with the first challenge.
    """
    print(f"Hello {player_name}, you just wake up and do not recognise the room around you. The last thing your remember is that you were at a dinner party with some friends and one of a sudden everything turned blurry. The room is completely empty except for some earplugs in one corner.\n")
    ear_plugs()


def ear_plugs():
    player_answer = input(f"Do you want to pick up the earplugs? y/n\n")
   
    if player_answer == 'y':
        print(f"The earplugs are now in your pocket, to get them type 'inventory' when needed.\n")
        return True
    if player_answer == 'n':
        return False
    if player_answer != 'y' or 'n':
        print(f"Invalid answer, please type 'y' or 'n' only.\n")
        return ear_plugs()


def door_choice():
    door_answer = input(f"\nThere are two doors in front of you, one is red, the other one is blue. You need to choose one, type 'red' or 'blue'.\n")

    if door_answer == 'blue':
        print("There is a hangry wolf in the room, the door is locked at your back. There is no escape, you die!\n")
        return game_over()
    if door_answer == 'red':
        return firebird_room()
    if door_answer != 'blue' or 'red':
        print(f"Invalid answer, please type 'blue' or 'red' only.\n")
        return door_choice()


def firebird_room():
    print('workout code for fire bird room')

def game_over():
    print('GAME OVER')


def main():
    """
    Calls all the functions in the game
    """
    start_room()
    door_choice()

main()