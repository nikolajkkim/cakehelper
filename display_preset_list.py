EXIT = -1
NEW = -2

def run(presets: list[str]) -> int:
    print(presets)
    print('You may choose an existing preset (1/2/3), you may create a new prest (new), or you may exit (exit).')
    preset_choice = input()

    # Return -1 if user wishes to exit.
    if preset_choice == "exit":
        return -1
    elif preset_choice == "new":
        return -2

    return int(preset_choice)-1

