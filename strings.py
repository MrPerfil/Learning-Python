###This is a guide to use strings.
##They're basically using variables inside a normal text.

# This prints out "Hello, Perfil!"
name="Perfil"
print("Hello, %s!" % name)
#(because "%s" tells the code to use a string, the "% name", and name="Perfil".)

##You can use more than one string in text.
email="perfiliwis@gmail.com"
username="mrperfil"
print ("Hi, %s, your new Email is %s" % (username, email))

##Here are the types of Strings.
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

##Oh, and, variables can have multiple values.
data = ("Perfil", "iwis", "negative 5.25")
format_string = "Hello %s%s. Your current balance is $%s."

print(format_string % data)