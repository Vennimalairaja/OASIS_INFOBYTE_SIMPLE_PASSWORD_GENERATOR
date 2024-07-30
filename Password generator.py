import string
import random
length=int(input("Enter the passowrd length: "))
print('''Choose character set for password from these:
         1.Digits
         2.Letters
         3.Special Characters
         4.Exit''')
characterList=""
while True:
    choice=int(input("Pick a number from above:"))
    if (choice==1):
        characterList+=string.ascii_letters
    elif choice==2:
        characterList+=string.digits
    elif choice==3:
        characterList+=string.punctuation
    elif choice==4:
        break
    else:
        print("Enter a valid choice:")
password=[]
for i in range(length):
    randomchar=random.choice(characterList)
    password.append(randomchar)
print("Your password is:"+"".join(password))