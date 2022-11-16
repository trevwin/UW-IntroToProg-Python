# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# TH,11.15.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# Step 1 - Additional Variables
objFile2 = [] # declare empty list for dummy var, original objFile is used as the file name
lstRow = [] # declare empty list
try:
    objFile2 = open(objFile, "r")
    for row in objFile2:
        lstRow = row.split(",") # returns a list
        dicRow = {"Task":lstRow[0], "Priority":lstRow[1].strip()}
        lstTable.append(dicRow) # this was added after encountering duplicate issues.
        # will use lstTable as the common up to date "table"
        print(dicRow)
    objFile2.close()
except: print("No text file found!")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks


    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable, "<<< Current updated table")
        objFile2.close()
        continue


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Get User Inputs / Declare new vars
        strTask = input("Please enter a Task:  ")
        strPrior = input("Please enter a Priority (low, medium, high):  ")
        dicRowInput = {"Task": strTask, "Priority": strPrior}  # new var to hold user input
        lstTable.append(dicRowInput) # append the user input to the list
        print(lstTable)
        print("Addition of new task and priority completed!")
        objFile2.close()
        continue


    # Step 5 - Remove a new Task from the list/Table
    elif (strChoice.strip() == '3'):
        # New Var's
        strRemove = input("Please type in Task or Priority to remove:  ")

        # Search for Task to remove
        for row in lstTable: # this is the most up to date list table of dictionary objects
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print("Row removed")
                print(lstTable, "<<< This is the updated table with your inputted task of: ", strRemove, " removed")
            else:
                print("Row not found")
        objFile2.close()
        continue


    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile2 = open(objFile, "w")
        for row in lstTable:
            objFile2.write(str(row["Task"]) + ',' + str(row["Priority"]) + '\n')
        objFile2.close()
        print("Tasks written to ToDoList.txt!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Program Exited!")
        break  # and Exit the program


