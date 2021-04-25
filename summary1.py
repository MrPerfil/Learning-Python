##To print text, use
print ("TEXT HERE")
##You can operate numbers in print, just without ""
print (1 + 2)
##Output should be 3

##This is a variable
variable1=1
variable2=2
##You can add Variables if they are numbers
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