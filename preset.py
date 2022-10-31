import dispense
import display_preset_list
import display_preset
import make_preset
import edit_preset

# If display_choices ever returns a -1, manual.py will immediately return to main.py, restarting the program.
EXIT = -1

def run():
    '''Main file calls this preset file. Runs the preset file.'''

    # Displays preset recipe section by reading from microsd file.
    # Preset layout... {preset#: 'compartment#-grams'}
    presets = [
        '1-30 2-40',
        '3-15',
        '1-20'
    ]
    
    while True:
        preset_choice = display_preset_list.run(presets)
        if preset_choice == -1:
            # Return back to main screen if user wishes to exit.
            return
        elif preset_choice == -2:
            # Create a new preset
            new_preset = make_preset.run()
            presets.append(new_preset)
            continue


        # Ask user if they would like to dispense or edit the preset.
        dispense_or_edit = display_preset.run(presets, preset_choice)

        if dispense_or_edit == "dispense":
            # Dispense chosen preset
            dispense.run(presets[preset_choice])
        elif dispense_or_edit == "edit":
            # Edit chosen preset
            new_preset = edit_preset.run(presets[preset_choice])
            presets[preset_choice] = new_preset
    
    return

