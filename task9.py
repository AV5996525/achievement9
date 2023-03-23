#Name:          achieve_9.py
#Author:        AJ Varatharajan
#Date Created:  February 23, 2023
#Date Last Modified: March 23, 2023
#Purpose: User is able to input student information and select courses by inputting the course code when prompted.
#
#This program will output the translation of the course code entered to it's respective course title along with student information. 
import os
from tabulate import tabulate
course = {} #initializing empty dictionary
course = {
    "ENG1221":"English",
    "CRE1342":"Careers",
    "NTB3070":"Networking Basics",
    "SCL1020":"Sociology"
}
stuInfo = {} #initializing empty dictionary
firstN = input("Enter your first name:") #Prompting input for field
stuInfo["First name"] = firstN #Adding input into dictionary associated with value
lastN = input("Enter your last name:") #Prompting input for field
stuInfo["Last name"] = lastN  #Adding input into dictionary associated with value
studN = input("Enter your student number:") #Prompting input for field
stuInfo["Student #"] = studN  #Adding input into dictionary associated with value
finL = []
courSel = {} #initializing empty dictionary
print(dict(course),"\nSelect your courses by entering any of these course codes: ENG1221, CRE1342 , NTB3070, SCL1020\nSeperate your choices with a ','") #printing course items stored in dictrionary
while True:
    try:
        courSel = input().split(",") #Prompting input for field
        for x in courSel:
            if x not in course.keys() and len(x) == 0:
                raise ValueError("2324")
            elif x not in course.keys() and len(x) >= 0:
                raise Exception("ABZXCDF")
        stuInfo["Course selection"] = courSel #Prompting input for field
    except ValueError: #except block - value error
        print("invalid entry")  
        exiQ = input("Do you want to exit?")
        if exiQ == "1":
            exit()
            break
        elif exiQ == '2':
            continue 
    except Exception: #except block - exception
         print("These course codes do not exist: ", list(courSel))
    finally:
        print("Your course registration summary:\n") #output title
        print(tabulate([[(stuInfo.get("First name"))], [(stuInfo.get("Last name"))], [(stuInfo.get("Student #"))]], headers = ["Student Information:"])) #output 
        print(tabulate([[('')]] , headers = ["Course's selected:"])) #output
        
        for x in courSel: # using for loop to cycle through each entry inputed by user
            print(course.get(x))
            finL.append(course.get(x))
            if x in course.keys(): #Checking if user registered for at least one course from the list
                newFile = open("schoolreport.txt", 'w') #If user selected at least one course, a file named "schoolreport.txt" will be created/accessed
                stuInfo["Total #"] = str(len(stuInfo["Course selection"])) 
                for y in stuInfo.items():#Looping through the items in the dictionary
                    newFile.write("{}\n".format(str(y)))#Writing the items accessed through the loop into the "schoolreport.txt" file
                    
        if x in course.keys(): #Checking if user registered for at least one course from the list
                newFile = open("schoolreport.txt", 'a') #If user selected at least one course, a file named "schoolreport.txt" will be created/APPENDED, not overwritten.
                newFile.write("These are your confirmed courses:\n") 
                for z,x in zip(finL, courSel):
                    newFile.write("{}\t{}\n".format(str(z),x))
                newFile.write("-------------------------------") 
        newFile.close()
        print("The summary txt file has been succesfully written to ", os.getcwd()) #Displaying file pathway
        print("File name: ", newFile) #Displaying file name "schoolreport.txt"
        




    

    











