from random import randint # import this so we can make a random number if the name is already taken

def infoGet(): # this gets the name from the user
    firstName = input("Please type your legal first name: ").lower().strip()
    middleName = input("Please type your middle initial (if multiple, seperate them with periods: ").lower().strip()
    lastName = input("Please type your legal last name: ").lower().strip()
    return(firstName, middleName, lastName) # return the three names to the makeName function
        
        
def makeName(): # this makes the name based on the info from infoGet
    firstName, middleName, lastName = infoGet() # make a basket for the info from infoGet
    name = firstName + "." + middleName + "." + lastName # ex. "john.d.doe"
    name = name.lower() # this is the fully-made name
    return(name) # send name to checkName

def checkName(): # this checks usernames.txt to see if name already exists
    number = randint(1, 70) # make a variable in case the name already exists
    name = makeName() # catch the value from makeName in a basket
    file = open("usernames.txt", "r") # open the username file
    for i in file.readlines(): # for every username in the usernames.txt file, do this
        if name.strip() == i.strip(): # if the name is already there,
            name = name + str(number) # add a number to it
    for i in file.readlines(): # do it again in case there are a lot of people with that name
        if name.strip() == i.strip(): # same as above
            name = name + str(number) # same as above
    file = open("usernames.txt", "a") # open file in append mode
    file.write("\n") # put a new line so they aren't right next to each other
    file.write(name) # write the name
    file.close() # close the file


    
checkName() # start the program by calling the checkName function
