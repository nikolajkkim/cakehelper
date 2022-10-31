

def run(presets: list[str], preset_choice: int) -> str:
    print("You have chosen preset " + str(preset_choice+1))
    value_list = presets[preset_choice].split() #['1-30', '2-40']
    for x in value_list:
        chosen_preset = x.split("-")
        compartment_used = chosen_preset[0]
        weight_used = chosen_preset[1]
        print("We have " + str(weight_used) + " grams from compartment " + str(compartment_used))
        
    print("Would you like to dispense this recipe or edit it?")
    dispense_or_edit = input()

    return dispense_or_edit