import display_choices
import dispense

# If display_choices ever returns a -1, manual.py will immediately return to main.py, restarting the program.
EXIT = -1

def run():
    '''Main file calls this manual file. Runs the manual file.'''

    # Dictionary that contains user inputs.
    # The key will be the compartment number.
    # The value will be the amount dispensed from the corresponding comparment.
    user_inputs = {}
    
    # Runs display_choices file.
    # display_choices file updates and returns new user_inputs dictionary with user inputs.
    user_inputs = display_choices.run(user_inputs)
    if user_inputs == -1:
        print("succesfully exited")
        return
    else:
        # Dispense what the user inputted.
        print(user_inputs)
        dispense.run(user_inputs)
    
    return
