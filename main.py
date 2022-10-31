import manual
import preset


def run():
    '''Main program on bootup. From here, user will decide on a manual screen or preset screen.'''

    while True:
        print("Please choose between manual or preset")
        choice = input() # choice will either be manual or preset
        if choice == "manual":
            manual.run()
        elif choice == "preset":
            preset.run()

        print("Back to the main screen.")



if __name__ == "__main__":
    run()