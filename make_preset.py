import display_choices

def run() -> str:
    new_value_str = ""
    print("Let's build your new preset!")

    while True:
        choice_list = display_choices.run()
        if choice_list == -1:
            # If user wishes to exit, we return -1 to preset.py
            return -1
        else:
            print("You have added " + choice_list[1] + " grams from compartment " + choice_list[0])
            
            # Update string containing new inputs
            new_value_str += str(choice_list[0]) + "-" + str(choice_list[1]+ " ")
            print("Would you like to add another ingredient? yes/no")
            extra_ingredient = input()
            if extra_ingredient == "no":
                break
            elif extra_ingredient == "yes":
                continue
    
    # Return collection of user's new inputs.
    return new_value_str[:-1]


    # CHANGE DISPLAY CHOICES TO RETURN A LIST INSTEAD OF DICT
    # CHANGE LIST TO DICT IN MANUAL.PY