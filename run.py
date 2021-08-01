print("\nWelcome to Adventureland, the adventure of you life!\n")

player_name = input("Pleaser enter your name: ")


def start_room():
    """
    Explains how to game works, what are the features and gets started with the first challenge.
    """
    print(f"\nHello {player_name}, you just wake up and do not recognise the room around you. The last thing your remember is that you were at a dinner party with some friends and one of a sudden everything turned blurry. The room is completely empty except for some earplugs in one corner.\n")

    player_answer = input(f"Do you want to pick up the earplugs? y/n\n")
    answer = input(f"{player_answer}").lower()

    if validate_answer(answer):
        return True


def validate_answer(answer):
    """
    Raises error if answer is not the expetected one by the player 
    """
    try:
        if player_name != "y" or "n" or "yes" or "no":
            raise ValueError(
                f"Please enter a valid answer: y/n or yes/no"
        )
    except ValueError as e:
        print(f"Invalid answer {e}, please try again.\n")
        return False
    return True


#    if player_name != "y" or "n" or "yes" or "no":
 #       print("Please enter a valid answer: y/n or yes/no")
  #  else:
   #     True


def main():
    """
    Calls all the functions in the game
    """
    start_room()
    validate_answer(start_room)

main()