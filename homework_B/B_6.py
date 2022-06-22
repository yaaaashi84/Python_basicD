import random

side = int(input("サイコロの面の数は?: "))
count = int(input("何回振りますか?: "))

def dice():
    return random.randint(1, count)

i = 0
list = []

for r in range(1, count+1):
    list.append(dice())

print(list)