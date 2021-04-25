mylist=[]
mylist.append(1) ##But print with ZERO!
mylist.append(2) ##But print with ONE!
print (mylist[0]) ##Will print ONE!
print (mylist[1]) ##Will print TWO!

##Remember, lists use in "print" are defined by NUMBER (0, 1, 2...) and NAME (mylist,dialog)

dialog=[]
dialog.append("Hi, im Perfil!") ##You can start lists in the number ZERO to make easier get the text ID.
dialog.append("Whats ur name?")
print (dialog[0])
print (dialog[1])


##Here is a test that was on the Learn Python page.
numbers = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)