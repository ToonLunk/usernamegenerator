username = 0
realname = 0
name = 0

print("*******************************\n")

name = input("\nWhat is your full name?\n\n ")
realname = str.lstrip(name)
realname = str.rstrip(name)
print("\n\n*****************************")
print("\n\nYour full name: ",str.title(realname),".\n\n")
print("********************************\n\n")

username = realname.replace(" ", ".")

print("Your Username is: ",username,".\n")
print("\n******************************")
