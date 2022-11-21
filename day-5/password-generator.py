# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pwd = ""
# for i in range(1, nr_letters+1):
#     ind = random.randint(0, len(letters)-1)
#     pwd += letters[ind]
# for i in range(1,nr_symbols+1):
#     ind = random.randint(0, len(symbols)-1)
#     pwd += symbols[ind]
# for i in range(1,nr_numbers+1):
#     ind = random.randint(0, len(numbers)-1)
#     pwd += numbers[ind]

pwd = ""
for i in range(1, nr_letters+1):
    pwd += random.choice(letters)
for i in range(1, nr_symbols+1):
    pwd += random.choice(symbols)
for i in range(1, nr_numbers+1):
    pwd += random.choice(numbers)


# Hard Level - Order of characters randomised:

# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# pwd2 = ""
# left_to_add = [nr_letters, nr_symbols, nr_numbers]
#
# while left_to_add[0] > 0 or left_to_add[1] > 0 or left_to_add[2] > 0:
#   rand_sel = random.randint(0,2)
#   if rand_sel == 0 and left_to_add[0] > 0:
#     ind = random.randint(0, len(letters)-1)
#     pwd2 += letters[ind]
#     left_to_add[0] -=1
#   elif rand_sel == 1 and left_to_add[1] > 0:
#     ind = random.randint(0, len(symbols)-1)
#     pwd2+=symbols[ind]
#     left_to_add[1] -=1
#   elif rand_sel == 2 and left_to_add[2] > 0:
#     ind = random.randint(0, len(numbers)-1)
#     pwd2+=numbers[ind]
#     left_to_add[2] -=1

pwd_list = []
for i in range(1, nr_letters+1):
    pwd_list.append(random.choice(letters))
for i in range(1, nr_symbols+1):
    pwd_list.append(random.choice(symbols))
for i in range(1, nr_numbers+1):
    pwd_list.append(random.choice(numbers))
random.shuffle(pwd_list)
pwd2 = ''.join(pwd_list)
print(pwd)
print(pwd2)
