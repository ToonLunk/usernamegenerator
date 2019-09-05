# usernamegenerator

I am in the process of creating a generic username generator, and will add more features (such as making sure that name isn't already taken) when I learn how to do so.

# Intention

This is to be made with the intention of generating a username based on the first name, middle initial, and last name of the user. It is *not* to be edited OR created by the user; as it's mainly for businesses and schools for generating an easy-to-identify username/email by just knowing their full name (with middle initial).

# Code Rules

The code needs to have a comment (#) for every function so that even a non-programmer can have a pretty good idea about what that line of code is doing. This will make troubleshooting easy, and easy for a company to edit the code themselves.

The user may *not* edit the username themselves. 

# Input Rules

The realName must be their full first and last name, with ONE middle initial used. Each name will be capitalized.

The username must be their full first name, followed by the first letter of their middle name, ending with their full last name; seperated with periods, with NO spaces in the name anywhere. See examples below.

If a username is not already taken, the username should be: "john.d.doe". If there is already a matching name, it should be "john.d.doe1","john.d.doe2" and so on.

# Example Input/Output

First name Input: tYler
Middle Initial Input: C
Last name Input: bROck

Output:

realName: Tyler C Brock
Username: tyler.c.brock
