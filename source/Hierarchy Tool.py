#!/usr/bin/env python3

############################################################
# Hierarchy Tool v.0.1                                     #
# created by Arseniy Arsentyew <programpro.ars@gmail.com>  #
############################################################
# This program is sharing with the GNU GPL.v3 license      #
############################################################

import os
import time

Constants = {"lineDelay": 0.02, "columDelay": 0.07}

class ConsoleAnimation():
    """The class with animation source"""

    def __init__(self):
        ''' Create empty colum '''
        self.colum = []

    def lineAnimate(self, lineToAnimate):
        ''' Animate string line '''
        for character in lineToAnimate:
            print(character, end="")
            time.sleep(Constants["lineDelay"])

    def addStringToColum(self, stringToAdd):
        ''' Add user's string to colum '''
        self.colum.append(stringToAdd)

    def columAnimate(self):
        ''' Animate current colum '''
        for i in self.colum:
            print(i)
            time.sleep(Constants["columDelay"])
        
class CreateHierarchy():
    """ 'Create' mode realisation """
    
    def __init__(self):
        ''' Initialise 'Create' mode '''
        self.consoleAnimator = ConsoleAnimation()

        print("\nStarting 'Create' mode")
        self.consoleAnimator.lineAnimate("######################\n\n")
        
        # choose the name and the path
        while True:
            try:
                self.path = input("Path to the folder: ")
                os.chdir(self.path)
                self.name = input("Name of the folder: ")
                os.mkdir(self.name)
                break
            except:
                print("! Path or name doesn't exist !\n")

        self.consoleAnimator.addStringToColum("\n###########################\n")
        self.consoleAnimator.addStringToColum("Launching Hierarchy Creator\n")
        self.consoleAnimator.addStringToColum("###########################\n\n")

        # Create root folder
        self.level = 1
        print(("#" * self.level) + " " + self.name)
        self.path = os.path.join(self.path, self.name)
        os.chdir(self.path)
        self.level += 2

        self.main()

    def main(self):
        ''' Main mode functionality method '''

        previosCommand = ""
        isFile = True

        # Main loop
        while True:
            self.consoleAnimator.lineAnimate((self.level * "#") + " ")
            lastCommand = input()

            # Exit condition
            if not(lastCommand):
                print("\n###################")
                print("# (Y)es - exit    #")
                print("# (N)o - continue #")
                print("###################")
                command = input("Your choice: ")
                if command.lower() == "y" or command.lower() == "yes":
                    break
                else:
                    continue
    
            # Path check
            if os.path.exists(os.path.join(self.path, lastCommand)):
                print("! This Name was used in the folder !")
                continue
            
            # Command condition
            if lastCommand == ">" and self.level != 3:
                self.level -= 2
                while self.path[-2] != '\\' and self.path[-2] != '/':
                    self.path = self.path[:-1]
                self.path = self.path[:-1] 
                os.chdir(self.path)
                continue
            elif lastCommand == ">":
                print("! You are on the root level !")
                continue
            elif lastCommand == "<" and isFile == True:
                print("! Command '<' doesn't work without directory name !")
                continue
            elif lastCommand == "<":
                self.level += 2
                self.path = os.path.join(self.path, previosCommand)
                os.chdir(self.path)
                previosCommand = lastCommand
                continue

            # File checking
            if lastCommand.find('.') == -1:
                isFile = False
            else:
                isFile = True

            # Create object
            try:
                if isFile:
                    with open(os.path.join(lastCommand), "w"):
                        pass
                else:
                    os.mkdir(os.path.join(self.path, lastCommand))
            except:
                print("! Creation Error !")
                continue

            previosCommand = lastCommand

class ManageHierarchy():
    """ 'Manage' mode realisation """
    pass

class Main():
    """ Main functionality """

    def __init__(self):
        ''' Start menu launching '''
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

        # Chose the tool
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

# Run program
if __name__ == "__main__":
    program = Main()