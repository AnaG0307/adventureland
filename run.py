def ear_plugs(inventory, player_answer):
    """
    Player can choose to pick the object 'earplugs', if the player chooses 'yes' the item gets 
    stored in the inventory function for future use.
    Requests yes/no answer from player to keep playing.
    Updates the inventory dictionary to True when object is picked.
    """
    if player_answer == 'yes':
        print(f"\nThe earplugs are now in your pocket, to get them type 'inventory' when needed.\n")
        inventory["earplugs"] = True
        return True
    if player_answer == 'no':
        return False
    if player_answer != 'yes' or 'no':
        print(f"Invalid answer, please type 'yes' or 'no' only.\n")
        return ear_plugs()


def door_choice():
    """
    Player can choose to go through red or blue door.
    Red door gets the player to the Firebird room and keeps playing.
    Blue door gets the player to the Wolf room and the game ends.
    Requests correct answer from player to keep playing.
    """
    door_answer = input(f"\nThere are two doors in front of you, one is red, the other one is blue. You need to choose one, type 'red' or 'blue'.\n")

    if door_answer == 'blue':
        print("\nThere is a hangry wolf in the room, the door is locked at your back. There is no escape, you die!\n")
        return game_over()
    if door_answer == 'red':
        return firebird_room()
    if door_answer != 'blue' or 'red':
        print(f"\nInvalid answer, please type 'red' or 'blue' only.\n")
        return door_choice()


def firebird_room():
    """
    Player needs to solve the Firebird's riddle
    """
    print('workout code for fire bird room')


def game_over():
    """
    Ends the game and asks the player if s/he wants to play again
    """
    print('GAME OVER')


def main():
    """
    Calls all the functions in the game
    """
    print("\nWelcome to Adventureland, the adventure of you life!\n")

    player_name = input(F"Pleaser enter your name: \n")

    s = \
"""Hello {}, you just wake up and do not recognise the room around you. The last thing your remember is that you were at a 
dinner party with some friends and one of a sudden everything turned blurry. The room is completely empty except for some 
earplugs in one corner.
""".format(player_name)

    print(s)

    player_answer = input(f"\nDo you want to pick up the earplugs? yes/no\n")

    inventory = {
        "earplugs": False
    }

    ear_plugs(inventory, player_answer)
    door_choice()


if __name__ == '__main__':
    main()