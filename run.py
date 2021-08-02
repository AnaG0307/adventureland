print("\nWelcome to Adventureland, the adventure of you life!\n")

player_name = input("Pleaser enter your name: ")


def start_room():
    """
    Explains how to game works, what are the features and gets started with the first challenge.
    """
    print(f"\nHello {player_name}, you just wake up and do not recognise the room around you. The last thing your remember is that you were at a dinner party with some friends and one of a sudden everything turned blurry. The room is completely empty except for some earplugs in one corner.\n")
    ear_plugs()

def ear_plugs():
    player_answer = input(f"Do you want to pick up the earplugs? y/n\n")
   
    if player_answer == 'y':
        print(f"The earplugs are now in your pocket, to get them type 'inventory'.\n")
        return True
    if player_answer == 'n':
        return False
    if player_answer != 'y' or 'n':
        print(f"Invalid answer, please type 'y' or 'n'.\n")
        return ear_plugs()




def main():
    """
    Calls all the functions in the game
    """
    start_room()

main()