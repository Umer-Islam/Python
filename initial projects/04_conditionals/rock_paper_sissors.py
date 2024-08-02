import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# rock wins scissors  // 0 wins 2
# scissors win paper// 2 wins 1
# paper wins rock //  1 wins 0
select = int(input('Enter 0 for rock, 1 for paper, 2 for scissors '))
computer_select = random.randint(0,2)
print(f'you selected {select}')
print(f'computer selected {computer_select}')



if select == computer_select:
    if select ==0:
        select=rock
    elif select ==1:
        select = paper
    elif select ==2:
        select = scissors
    if computer_select ==0:
        computer_select=rock
    elif computer_select ==1:
        computer_select = paper
    elif computer_select ==2:
        computer_select = scissors
    
    print(f'You:{select}\nDraw try again\n computer:{computer_select}')
elif (select == 0 and computer_select == 2) or(computer_select == 0 and select == 2):
    if select ==0:
        select=rock
    elif select ==1:
        select = paper
    elif select ==2:
        select = scissors
    if computer_select ==0:
        computer_select=rock
    elif computer_select ==1:
        computer_select = paper
    elif computer_select ==2:
        computer_select = scissors
    
    
    print(f'You:{select}\n rock WINS\n computer:{computer_select}')
elif (select == 2 and computer_select==1) or (computer_select==2 and select == 1):
    if select ==0:
        select=rock
    elif select ==1:
        select = paper
    elif select ==2:
        select = scissors
    if computer_select ==0:
        computer_select=rock
    elif computer_select ==1:
        computer_select = paper
    elif computer_select ==2:
        computer_select = scissors
    
    print(f'You:{select}\n Scissors WIN\n computer:{computer_select}')
elif (select ==1 and computer_select==0) or (computer_select==1 and select ==0):
    if select ==0:
        select=rock
    elif select ==1:
        select = paper
    elif select ==2:
        select = scissors
    if computer_select ==0:
        computer_select=rock
    elif computer_select ==1:
        computer_select = paper
    elif computer_select ==2:
        computer_select = scissors
    
    print(f'You:{select}\n paper WINS\n computer:{computer_select}')
else:
    print('please enter a number between 0 and 2')