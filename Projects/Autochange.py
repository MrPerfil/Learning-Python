###THE PROJECT IS NOT MINE! It's just a great idea.
a = 0
b = 1
print (a + b)

content = []
with open(__file__,"r") as f:
    for line in f:
        content.append(line)

with open(__file__,"w") as f:
    content[1] = "a = {n}\n".format(n=b)
    content[2] = "b = {n}\n".format(n=a+b)
    for i in range(len(content)):
        f.write(content[i])