import display_choices

def run(preset: str) -> str:
    new_value_str = ""
    print("Let's edit your preset!")
    preset = [preset]

    
    if " " in preset[0]:
        preset = preset[0].split(" ")
    preset_dict = {}
    for x in preset:
        preset_dict[x[0]] = x[2:]
    print(preset_dict)
    print("----------------")
    print("Here is your current preset")
    for x in range(1, 5):
        if str(x) in preset_dict:
            print("Compartment " + str(x) + ": " + str(preset_dict[str(x)]) + " grams")
        else:
            print("Compartment " + str(x) + ": 0 grams")


    while True:
        choice_list = display_choices.run()
        if choice_list == -1:
            return -1
        else:
            print("You are now dispensing " + choice_list[1] + " grams from compartment " + choice_list[0])
            preset_dict[choice_list[0]] = choice_list[1]
            print("Would you like to add another ingredient? yes/no")
            extra_ingredient = input()
            if extra_ingredient == "no":
                break
            elif extra_ingredient == "yes":
                continue

    for key in preset_dict.keys():
        new_value_str += key + "-" + preset_dict[key]

    return new_value_str[:-1]


    # CHANGE DISPLAY CHOICES TO RETURN A LIST INSTEAD OF DICT
    # CHANGE LIST TO DICT IN MANUAL.PY