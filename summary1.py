##To print text, use
print ("TEXT HERE")
##You can operate numbers in print, just without ""
print (1 + 2)
##Output should be 3

##This is a variable
variable1=1
variable2=2
##You can add Variables if they are plain numbers
print (variable1 + variable2)
##Output should be 3, because 1+2=3
##You can also add text using variables, the text will just appear together
text1="Hello"
text2="World"
print (text1 + text2)
##There will be no space you must add the space yourself
space=" "
print (text1 + space + text2)
##You will get errors if you print a variable that does not exits.
##I won't do that because that would crash the entire script.

##You can make numbers act like text, just adding ""
numberistext1="1"
numberistext2="2"
print (numberistext1 + numberistext2)

##You can also make aliases for the variables.
##Frist make the original variable
original="This is the text"
##And then another variablem but the context of it is another variable.
alias=original
##And the you can print it using the name of the frist variable (original) or the alias.
print (alias)
print (original)

##This is a list
mylist=[]
mylist.append("This is the frist line")
mylist.append("This is the second line")
mylist.append("You can put numbers too!")
mylist.append(1)
##To use them in commands like Print,
print (mylist[0])
##Remember, the list starts in ZERO, so the first line is represented with the number 0, and the second with the number 1.

##You can't combine the use of lists and plain numbers or text
print (mylist[3] + 2)
##Output will be 3, not 5.

###FROM and IMPORT
#s#This is a guide to import variables from other files!
##Command FROM <file> import <variable> will do all the work
from from_import2 import dialog1
##You only can import ONE VARIABLE at a time.
print (dialog1)
##Now, look for the dialog1 variable in THIS file! u will never find it.

##Can you import ENTIRE lists?
from from_import2 import list
print (list[0])
##YEAH, YOU CAN LOL!
#(Importing list can save you a lot of work)
#(If you import variable and variable, you will to write a LOT of code.)

##NOTE= If you run a python file with FROM command and the second file has errors, the output will show you erros in the other file too.
#(for example, file1.py uses "from file2.py" but file2.py has a bad syntax. Output will show that.)