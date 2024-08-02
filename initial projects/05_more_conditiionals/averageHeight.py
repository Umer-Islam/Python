# write to find average height:
# i. ask user to input different heights, turn them into array using split()
# ii. do not use len() and sum()
heights = input('please enter heights separated by a space in cm').split()
for n in range(0, len(heights)):
    heights[n]= int(heights[n])
total_height =0
for x in heights:
    total_height+=x
print(total_height)

for people in heights:
    people+=1

print(people-1)

average = total_height /(people-1)
print(average)