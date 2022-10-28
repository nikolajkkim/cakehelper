import manual

def run(user_inputs: dict):
    '''Given a dictionary of user inputs, dispesne the proper amount of each compartment.'''

    for compartment in user_inputs:
        # Will have code for telling raspberry pi to dispense 
        print("we have dispensed " + str(user_inputs[compartment]) + " in compartment " + str(compartment))

    return