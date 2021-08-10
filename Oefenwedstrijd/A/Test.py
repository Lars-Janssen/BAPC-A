import random

f = open("test2.txt", "a")
n = 333333
string = ""
for i in range(n):
    string = string + "LBR"
print(string, file=f)
f.close()