import main

def run() -> int:
    '''Runs display numpad file. Returns the number that the user chooses.'''

    # Present display for users here.
    print("How much would you like?")

    #input from user is stored in variable user_compartment
    user_comparment = input() 

    # Contains an exit button.
        # If exit button is pressed, return -1
    # Contains a back button.
        # If back button is pressed, return -2 
    if user_comparment == "exit":
        return -1
    elif user_comparment == "back":
        return -2

    return user_comparment
