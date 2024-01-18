""" take an array of numbers and find max and min numbers without using functions like max() or min() """
scores = input('please enter scores separated by a space').split()
for n in range(0, len(scores)):
    scores[n]= int(scores[n])
highest =0
for score in scores:
    if score > highest:
        highest = score
print(highest)

lowest = scores[0]
for score in scores:
    if lowest <score:
        lowest =score
print(lowest)
