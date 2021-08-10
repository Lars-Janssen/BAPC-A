import random

f = open("A2.txt", "a")
metals = 1000
experiments = random.randint(0, 499500)
print(metals, experiments, file=f)

for i in range(experiments):
    x = random.randint(0,metals - 1)
    y = random.randint(0,metals - 1)

    while(x == y):
        y = random.randint(1, )

    print(x, y, file=f)
f.close()