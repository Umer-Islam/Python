import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '|', '[', ']', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
lowercase_letters = []
uppercase_letters = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

userNumbers = int(input('how many numbers do you want?\n'))
userSpecialCharacters = int(input('how many special characters do you want?\n'))
userLetters = int(input('how many letters do you want?'))
password = []
# # random numbers
for number in range(userNumbers):
    randomNumber = random.randint(0,9)
    print(randomNumber)
    password += str(randomNumber)

for character in range(userSpecialCharacters):
    randomChar = random.randint(0,9)
    print(special_characters[randomChar])
    password += special_characters[randomChar]


for letter in range(userLetters):
    randomletter = random.randint(0,9)
    print(letters[randomletter])
    password += letters[randomletter]



print(f'{password} before shuffle')
random.shuffle(password)
print(f'{password} after shuffle')

passwordStr = ''
for char in password:
    passwordStr+=char
print(passwordStr)


