# Day:3 Q5
# check whether an year is leap year or not
# 3 conditions must for leap year:
# year/4 //true
# year/100 //False
# year/400 // true
year = int(input('enter year'))
if year%4 ==0:
  if year%100 !=0:
    print('Not leap 1')
  elif year%400:
    print('leap Year 2')
  else:
   print('leap year 3') 
