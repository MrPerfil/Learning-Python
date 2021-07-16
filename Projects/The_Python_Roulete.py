##Right now, we know how to print, use variables, import, use dices and conditions. Let's do a roulete!

#Frist we need a dice. 
import random
dice=random.randint(1,6)
#We made the dice. It has 6 posibilities
#Now we need a conditions chain. 
if dice == 1:
    print ("One point! It's sad.")
if dice == 2:
    print ("Two points! It's still really low...")
if dice == 3:
    print ("Three points! like my IQ!")
if dice == 4:
    print ("Four points! Two times two times one!")
if dice == 5:
    print ("Five points! Like the numbers of hands of a human! Wait...")
if dice == 6:
    print ("Six points! The lucky number!")

#Now, we just made a roulete.