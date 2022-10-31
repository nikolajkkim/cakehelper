import main
import display_compartment
import display_numpad

# File prompts user to choose a compartment and a numpad. 
# Updates and returns a dictionary containing the new choices.

# If display_compartment or display_choices return either of the following two
# negative numbers, the program will either exit, or go back.
EXIT = -1
BACK = -2

def run() -> list[str]:
    '''Takes the current dictionary of user inputs. Requests new inputs from user
    and updates + returns the new dictionary.'''

    while True:
        # Display comparment to user.
        user_compartment = display_compartment.run()
        if user_compartment == -1:
            # if user hits "exit" from compartment, will go back to previous file.
            return -1

        # Display numpad to user.
        user_num = display_numpad.run()
        if user_num == -1:
            # if user hits "exit" from numpad, will go back to previous file.
            return -1
        elif user_num == -2:
            # if user hits "back" from numberpad, will go back to display_compartment.
            continue

        # Add compartment and number to dictionary
        returning_values = [user_compartment, user_num]
        break


    return returning_values