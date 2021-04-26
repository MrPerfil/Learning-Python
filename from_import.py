##This is a guide to import variables from other files!
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