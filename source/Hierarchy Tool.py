
############################################################
# Hierarchy Tool                                           #
# created by Arseniy Arsentyew <programpro.ars@gmail.com>  #
############################################################
# This program is sharing with the GNU GPL.v3 license      #
############################################################

class ConsoleAnimation():
    """The class with animation source"""

    def __init__(self):
        self.colum = []

    def lineAnimate(self, lineToAnimate):
        for character in lineToAnimate:
            print(character, end="")
        print("\n", end="")

    def addStringToColum(self, stringToAdd):
        self.colum.append(stringToAdd)

    def columAnimate(self):
        for i in self.colum:
            print(i)
        
class CreateHierarchy():
    """ 'Create' mode realisation """
    pass

class ManageHierarchy():
    """ 'Manage' mode realisation """
    pass

class Main():
    """ Main functionality """

    def __init__(self):
        consoleAnimator = ConsoleAnimation()
        consoleAnimator.addStringToColum("##########")
        consoleAnimator.addStringToColum("Created by")
        consoleAnimator.addStringToColum("Arseniy Arsentyew <programpro.ars@gmail.com>")
        consoleAnimator.addStringToColum("############################################")
        consoleAnimator.addStringToColum("  _  _ _                     _")
        consoleAnimator.addStringToColum(" | || (_)___ _ _ __ _ _ _ __| |_ _  _")
        consoleAnimator.addStringToColum(" | __ | / -_) '_/ _` | '_/ _| ' \ || |")
        consoleAnimator.addStringToColum(" |_||_|_\___|_| \__,_|_| \__|_||_\_, |")
        consoleAnimator.addStringToColum(" |_   _|__  ___| |               |__/")
        consoleAnimator.addStringToColum("   | |/ _ \/ _ \ |")
        consoleAnimator.addStringToColum("   |_|\___/\___/_|")
        consoleAnimator.addStringToColum("")
        consoleAnimator.addStringToColum("############################################")
        consoleAnimator.addStringToColum("")
        consoleAnimator.addStringToColum("Choose the mode:")
        consoleAnimator.addStringToColum("")
        consoleAnimator.addStringToColum('1. "Create" (0)')
        consoleAnimator.addStringToColum('2. "Manage" (1)')
        consoleAnimator.addStringToColum("")

        consoleAnimator.columAnimate()
        while True:
            mode = input("Your choice: ")

            if mode == "0" or mode.lower() == "create":
                modeManager = CreateHierarchy()
                break
            elif mode == "1" or mode.lower() == "manage":
                modeManager = ManageHierarchy()
                break
            else:
                print("Select mode from the list:")
                print("\n", end="")
                print('1. "Create" (0)')
                print('2. "Manage" (1)')
                print("\n", end="")


if __name__ == "__main__":
    program = Main()