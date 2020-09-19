#!/usr/bin/env python3

############################################################
# Hierarchy Tool v.0.1                                     #
# created by Arseniy Arsentyew <programpro.ars@gmail.com>  #
############################################################
# This program is sharing with the GNU GPL.v3 license      #
############################################################

# Fix the error
import os
import re
import time
import shutil
import webbrowser
 
Constants = {"urlLink": "https://github.com/programpro-ars/Hierarchy-Tool/tree/master/documentation",
            "lineDelay": 0.01, "columDelay": 0.05, "levelStep": 3}

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
    ''' Class for the search using regular expressions '''
    def __init__(self):
        self.number = 1

    def find(self, regular_expression):
        resultList = []
        try:
            template = re.compile(regular_expression)
        except:
            print("\n! An error in the regular expression !\n")
            return []
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

    def get_nums(self, count):
        self.number += 1
        return self.number - 1

    def restart_nums(self):
        self.number = 1

    def set_custom(self, customMethod):
        pass

    def get_custom(self):
        pass

    def search(self, reregular_expression):
        resultList = []
        try:
            template = re.compile(regular_expression)
        except:
            print("\n! An error in the regular expression !\n")
            return []
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
    """ Main functionality """

    def __init__(self):
        """ Initialise the tool """
        self.consoleAnimator = ConsoleAnimation()
        self.regularSearch = RegularSearch()
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
        if self.level == 1:
            print("\n! You are on the root level !\n")
        else:
            self.level -= Constants["levelStep"]
            while self.path[-2] != os.sep:
                self.path = self.path[:-1]
            self.path = self.path[:-1] 
            os.chdir(self.path)

    def getCurrentPlace(self):
        print(self.path)

    def showAll(self):
        number = 1
        for obj in os.listdir(self.path):
            print("*" * self.level + "  " + str(number) + ") " + obj)
            number += 1

    def goDown(self, folder_name):
        try:
            if os.path.exists(os.path.join(self.path, folder_name)):
                self.path = os.path.join(self.path, folder_name)
                os.chdir(self.path)
                sepCount = folder_name.count(os.path.sep)
                self.level += Constants["levelStep"] * (sepCount + 1)
            else:
                print("\n! Folder " + folder_name + " does not exist !\n")
        except:
            print("\n! Path changing error !\n")

    def create(self, object_name):
        if os.path.exists(os.path.join(self.path, object_name)):
            print("\n! This name was used in the current folder !\n")
            return

        if object_name.find('.') == -1:
            isFile = False
        else:
            isFile = True

        try:
            if isFile:
                with open(os.path.join(object_name), "w"):
                    pass
            else:
                os.mkdir(os.path.join(self.path, object_name))
            print("*" * self.level + " comlete")
        except:
                print("\n! Creation error !\n")
        
    def delete(self, regular_expression):
        objsToDelete = self.regularSearch.find(regular_expression)
        for obj in objsToDelete:
            if os.path.isfile(os.path.join(self.path, obj)):
                os.remove(os.path.join(self.path, obj))
            else:
                shutil.rmtree(os.path.join(self.path, obj))
            print("*" * self.level + " " + obj + " has been deleted")

    def search(self, regular_expression):
        objectsToFind = self.regularSearch.search(regular_expression)
        number = 1
        for obj in objectsToFind:
            print(" " * (self.level + 2) + str(number) + ") " + obj)
            number += 1

    def rename(self, previous_names, new_names):
        pass

    def move(self, regular_expression, new_path):
        objectsToMove = self.regularSearch.find(regular_expression)
        if not(os.path.exists(os.path.join(new_path))):
            print("\n! The path does not exists !\n")
            return

        for obj in objectsToMove:
            if os.path.exists(os.path.join(new_path, obj)):
                print("! " + obj + " is exists in " + new_path + " !")
            else:
                try:
                    shutil.move(os.path.join(self.path, obj), os.path.join(new_path, obj))
                    print("*" * self.level + " " + obj + " has been moved")
                except:
                    print("! An error while " + obj + " moving !")

    def copy(self, regular_expression, new_path):
        pass

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

# Run program
if __name__ == "__main__":
    program = Start()