#!/usr/bin/env python3

############################################################
# Hierarchy Tool v.1.0                                     #
# created by Arseniy Arsentyew <programpro.ars@gmail.com>  #
############################################################
# This program is sharing with the GNU GPL.v3 license      #
############################################################

import os
import re
import time
import shutil
import webbrowser

# Some custom values
Constants = {"urlLink": "https://github.com/programpro-ars/Hierarchy-Tool/tree/master/documentation",
            "lineDelay": 0.01, "columDelay": 0.05, "numsLiteral": "<nums>", "customLiteral": "<custom>"}

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

class RegularSearch():
    ''' Class for the searching using regular expressions '''

    def __init__(self):
        ''' Initialise custom generator '''
        self.set_custom()

    def find(self, regular_expression):
        ''' Find objects in current folder '''
        resultList = []
        # Compiling the regular expression 
        try:
            template = re.compile(regular_expression)
        except:
            print("\n! An error in the regular expression !\n")
            return []
        # Finding goal objects
        for root, dirs, files in os.walk("."):
            for obj in dirs:
                result = template.match(os.path.join(root, obj)[2:])
                if result == None:
                    continue
                if result.group() == os.path.join(root, obj)[2:]:
                    resultList.append(os.path.join(root, obj)[2:])
            for obj in files:
                result = template.match(os.path.join(root, obj)[2:])
                if result == None:
                    continue
                if result.group() == os.path.join(root, obj)[2:]:
                    resultList.append(os.path.join(root, obj)[2:])
        return resultList

    def get_nums(self):
        ''' Get next number '''
        self.number += 1
        return self.number - 1

    def restart_nums(self):
        ''' Restart number generator '''
        self.number = 1

    def set_custom(self):
        ''' Set custom method '''
        # replace 'None' with the names of your functions
        self.customGet = None
        self.customRestart = None

    def get_custom(self):
        ''' Get next custom value '''
        if self.customGet == None:
            return "DOESN'T EXISTS"
        else:
            return self.customGet()

    def restart_custom(self):
        ''' Restart custom generator '''
        if self.customRestart == None:
            print("\n! Custom generator doesn't exists !")
            print("! for more information write 'help' command !\n")
        else:
            self.customRestart()

    def search_item(self, regular_expression):
        ''' Find objects in current tree '''
        resultList = []
        # Compiling the regular expression
        try:
            template = re.compile(regular_expression)
        except:
            print("\n! An error in the regular expression !\n")
            return []
        # Finding goal objects
        for root, dirs, files in os.walk("."):
            for obj in dirs:
                result = template.match(obj)
                if result == None:
                    continue
                if result.group() == obj:
                    resultList.append(os.path.join(root, obj)[2:])
            for obj in files:
                result = template.match(obj)
                if result == None:
                    continue
                if result.group() == obj:
                    resultList.append(os.path.join(root, obj)[2:])
        return resultList
    
class HierarchyTool():
    """ The class with main functionality """

    def __init__(self):
        """ Initialise the tool """
        self.consoleAnimator = ConsoleAnimation()
        self.regularSearch = RegularSearch()
        self.increaseList = []
        self.level = 1

        # choose the path
        while True:
            try:
                self.path = input("Path to the folder: ")
                os.chdir(self.path)
                break
            except:
                print("\n! Path doesn't exist !\n")
                continue

        self.consoleAnimator.addStringToColum("\n###########################\n")
        self.consoleAnimator.addStringToColum("Launching Hierarchy Manager\n")
        self.consoleAnimator.addStringToColum("###########################\n\n")

        print("\n-- " + self.path + " --")
        print('-' * (len(self.path) + 6))

        self.rootPath = self.path
        self.main()

    def main(self):
        """ Command Runner """

        # main loop
        while True:
            self.consoleAnimator.lineAnimate("#" * self.level + ": ")
            userInput = input()

            # Exit condition
            if not(userInput):
                print("\n###################")
                print("# (Y)es - exit    #")
                print("# (N)o - continue #")
                print("###################")
                command = input("Your choice: ")
                if command.lower() == "y" or command.lower() == "yes":
                    print("\n", end="")
                    break
                else:
                    print("\n", end="")
                    continue

            # Fast commands condition
            if len(userInput) == 1:
                if userInput == ">":
                    self.goTop()
                    continue
                elif userInput == "?":
                    self.getCurrentPlace()
                    continue
                elif userInput == "*":
                    self.showAll()
                    continue
                else:
                    print("\n! Unknown command !\n")
                    continue

            # Format the user input
            if userInput[-1] == "<":
                userInput = userInput[:-2]
                self.goDown(userInput)
                continue
            else:
                wordSize = 0
                for letter in userInput:
                    if letter != " ":
                        wordSize += 1 
                    else:
                        break 

                currentCommand = userInput[:wordSize]
                userInput = userInput[wordSize + 1:]

            # Run simple commands
            if currentCommand == "cr" or currentCommand == "create":
                self.create(userInput)
            elif currentCommand == "dl" or currentCommand == "delete":
                self.delete(userInput)
            elif currentCommand == "sr" or currentCommand == "search":
                self.search(userInput)
            elif currentCommand == "help":
                webbrowser.open(Constants["urlLink"], new=2)
            else:
                # Setup some values
                leftSide = ""
                rightSide = ""
                isLeftSide = True
                userInput = list(userInput.split(" "))

                # Separate the user input
                for word in userInput:
                    if word != "->":
                        if isLeftSide:
                            leftSide += word + " "
                        else:
                            rightSide += word + " "
                    else:
                        isLeftSide = False

                # Run complex commands
                if isLeftSide:
                    print("\n! Wrond command !\n")
                else:
                    leftSide = leftSide[:-1]
                    rightSide = rightSide[:-1]
                    if currentCommand == "rn" or currentCommand == "rename":
                        self.rename(leftSide, rightSide)
                    elif currentCommand == "mv" or currentCommand == "move":
                        self.move(leftSide, rightSide)
                    elif currentCommand == "cp" or currentCommand == "copy":
                        self.copy(leftSide, rightSide)
                    else:
                        print("\n! Unknown command !\n")

    def goTop(self):
        ''' Changing path to the parent folder '''
        if self.level == 1:
            print("\n! You are on the root level !\n")
        else:
            while self.path[-2] != os.sep:
                self.path = self.path[:-1]
            self.path = self.path[:-1] 
            os.chdir(self.path)
            self.level -= (self.level - self.increaseList[-1])
            del self.increaseList[-1]
            print("\n", end="")

    def getCurrentPlace(self):
        ''' Get current path ''' 
        print((self.level - 1) * " " + "*" + "  " + self.path)

    def showAll(self):
        ''' Print all objects in the current folder '''
        number = 1
        for obj in os.listdir(self.path):
            print((self.level - 1) * " " + "*" + "  " + str(number) + ") " + obj)
            number += 1

    def goDown(self, folder_name):
        ''' Changing path to the next folder '''
        try:
            if os.path.exists(os.path.join(self.path, folder_name)):
                self.path = os.path.join(self.path, folder_name)
                os.chdir(self.path)
                sepCount = folder_name.count(os.path.sep)
                self.increaseList.append(self.level)
                self.level += len(folder_name) + 4
                newLevelName = self.path
                newLevelName = newLevelName.replace(self.rootPath, " ")[2:]
                print("\n# " + newLevelName.replace(os.sep, " * "))
            else:
                print("\n! Folder " + folder_name + " does not exist !\n")
        except:
            print("\n! Path changing error !\n")

    def create(self, object_name):
        ''' Create object '''
        # Checking path existence
        if os.path.exists(os.path.join(self.path, object_name)):
            print("\n! This name was used in the current folder !\n")
            return
        # Get object type
        if object_name.find('.') == -1:
            isFile = False
        else:
            isFile = True
        # Create object
        try:
            if isFile:
                with open(os.path.join(object_name), "w"):
                    pass
            else:
                os.mkdir(os.path.join(self.path, object_name))
            print((self.level - 1) * " " + "*" + " " + " comlete")
        except:
            print("\n! Creation error !\n")
        
    def delete(self, regular_expression):
        ''' Delete objects '''
        objsToDelete = self.regularSearch.find(regular_expression)
        # Deleting current objects
        for obj in objsToDelete:
            if os.path.isfile(os.path.join(self.path, obj)):
                os.remove(os.path.join(self.path, obj))
            else:
                shutil.rmtree(os.path.join(self.path, obj))
            print((self.level - 1) * " " + "*" + "  " + obj + " has been deleted")

    def search(self, regular_expression):
        ''' Search tree for the needed objects '''
        objectsToFind = self.regularSearch.search_item(regular_expression)
        number = 1
        for obj in objectsToFind:
            print((self.level - 1) * " " + "*" + "  " + str(number) + ") " + obj)
            number += 1

    def rename(self, previous_names, new_names):
        ''' Rename objects '''
        objectsToRename = self.regularSearch.find(previous_names)
        generatorFunction = None
        startIndex = 0
        endIndex = 0
        # Checking for generators
        if new_names.find(Constants["numsLiteral"]) != -1:
            startIndex = new_names.find(Constants["numsLiteral"])
            endIndex = startIndex + len(Constants["numsLiteral"])
            new_names.replace(Constants["numsLiteral"], "")
            generatorFunction = self.regularSearch.get_nums
            self.regularSearch.restart_nums()
        elif new_names.find(Constants["customLiteral"]) != -1:
            startIndex = new_names.find(Constants["customLiteral"])
            endIndex = startIndex + len(Constants["customLiteral"])
            new_names.replace(Constants["customLiteral"], "")
            generatorFunction = self.regularSearch.get_custom
            self.regularSearch.restart_custom()
        # Renaming objects
        for obj in objectsToRename:
            if generatorFunction == None:
                currentName = new_names
            else:
                currentName = new_names[:startIndex] + str(generatorFunction()) + new_names[endIndex:]
            
            try:
                os.rename(obj, currentName)
                print((self.level - 1) * " " + "*" + "  " + obj + " has been renamed to " + currentName)
            except:
                print("! " + obj + " can not be renamed !")

    def move(self, regular_expression, new_path):
        ''' Move objects '''
        objectsToMove = self.regularSearch.find(regular_expression)
        # Checking path existence
        if not(os.path.exists(os.path.join(new_path))):
            print("\n! The path does not exists !\n")
            return
        # Moving objects
        for obj in objectsToMove:
            if os.path.exists(os.path.join(new_path, obj)):
                print("! " + obj + " is exists in " + new_path + " !")
            else:
                try:
                    shutil.move(os.path.join(self.path, obj), os.path.join(new_path, obj))
                    print((self.level - 1) * " " + "*" + "  " + obj + " has been moved")
                except:
                    print("! An error while " + obj + " moving !")

    def copy(self, regular_expression, new_path):
        ''' Copy objects '''
        objectsToCopy = self.regularSearch.find(regular_expression)
        # Copying objects
        for obj in objectsToCopy:
            if os.path.exists(os.path.join(new_path, obj)):
                print("! " + obj + " is exists in " + new_path + " !")
            else:

                try:
                    if os.path.isfile(obj):
                        shutil.copy(os.path.join(self.path, obj), os.path.join(new_path, obj))
                    else:
                        shutil.copytree(os.path.join(self.path, obj), os.path.join(new_path, obj))
                    print((self.level - 1) * " " + "*" + "  " + obj + " has been copied")
                except:
                    print("! Can not copy " + obj + ' !')
        

class Start():
    """ Start the program """

    def __init__(self):
        ''' 'Start Menu' launching '''
        consoleAnimator = ConsoleAnimation()
        consoleAnimator.addStringToColum("\n##########")
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

        consoleAnimator.columAnimate()

        startProgram = HierarchyTool()

# Run the program
if __name__ == "__main__":
    program = Start()