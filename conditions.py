###Python can use basic Boolean logic (True or false)
##In Math,
x=2
print (x == 2) #Will print true, because yeah, X is two
print (x == 3) #Will print false, beacuse X is NOT 3
#It also works with < or >, and even math operations or variables
print (x < 3) #Will print True, because 2 is less than 3
print (x == 4-2) #Will print two, because X = 2 [4-2=2]

##But with IF, AND, OR,
name="Perfil"
age=12
if name == "Perfil" and age == 12:
    print("Your name is Perfil, and you are also 12 years old.")

if name == "Perfil" or "Luis":
    print("idk ur name bro maybe its luis and maybe is perfil xd")

#It won't print things if it's false

test="Hello!"
if test == "Goodbye!":
    print("bruh")

#You're not limited to just Print things. You can use IF, AND & OR before any command, usually it does not have sense if the command is not something interactive, like print.
#This can be used in videogames, for example, IF charecter is at X_position, print "You are here!", or something.
