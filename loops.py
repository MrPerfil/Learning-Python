#(not important)
space=" "
###This is a guide about loops in Phyton
##There's two types of loops in python, for and while

##For  
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime) #(will print those numbers [2, 3, 5, 7])

print (space)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x) #(will print from 0 to 4)

print (space)
# Prints out 3,4,5
for x in range(3, 6):
    print(x) #(will print from 3 to 5)

print (space)
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x) #(I don't understand this one. Sorry.)

print (space)
print (space)

##Remenber, if the For time is used with Range, the Max won't count. 
#(for example, 3 to 6, only 3; 4 and 5.)

##While
count = 0
while count < 5:
    print(count) 
    count += 1  #(will print until it reachs 4)