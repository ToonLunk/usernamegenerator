from random import randint

def infoGet():
    firstName = input("Please type your legal first name: ").lower()
    middleName = input("Please type your middle initial: ").lower()
    lastName = input("Please type your legal last name: ").lower()
    return(firstName, middleName, lastName)
        
        
def makeName():
    firstName, middleName, lastName = infoGet()
    name = firstName + "." + middleName + "." + lastName
    name = name.lower()
    return(name)

def checkName():
    number = randint(1, 70)
    name = makeName()
    file = open("usernames.txt", "r")
    for i in file.readlines():
        if name.strip() == i.strip():
            name = name + str(number)
    for i in file.readlines():
        if name.strip() == i.strip():
            name = name + str(number)
    file = open("usernames.txt", "a")
    file.write("\n")
    file.write(name)
    file.close()


    
checkName()
