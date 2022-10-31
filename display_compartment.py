import main

def run() -> int:
    '''Runs display comparment file. Returns the comparment that the user chooses.'''
    
    # Present display for users here.
    print("What compartment would you like to choose?")

    #input from user is stored in variable user_compartment
    user_comparment = input() 

    # Contains an exit button.
        # If exit button is pressed, return -1

    if user_comparment == "exit":
        return -1

        



    return user_comparment