import random

names = input("enter names with comma(,) after every name\n")
nameList = names.split(", ")

length = random.randint(0, len(nameList) - 1)
print(len(nameList))
print(f"{nameList[length]}, will pay for todays meal")
