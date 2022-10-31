import manual

def run(user_inputs: list[str]):
    '''Given a dictionary of user inputs, dispesne the proper amount of each compartment.'''
    user_inputs = user_inputs.split(" ")
    for dispense_clump in user_inputs:
        # Will have code for telling raspberry pi to dispense 
        dispense_list = dispense_clump.split("-")
        print("we have dispensed " + str(dispense_list[1]) + " grams in compartment " + str(dispense_list[0]))

    return