# # Write your code below this line ๐
# from math import sqrt


# def prime_checker(number):
#     if n <= 1:
#         print("It's not a prime number.")
#         return

#     for i in range(2, int(sqrt(number))+1):
#         if number % i == 0:
#             print("It's not a prime number.")
#             return
#     print("It's a prime number.")


# # Write your code above this line ๐

# # Do NOT change any of the code below๐
# n = int(input("Check this number: "))
# prime_checker(number=n)


# Write your code below this line ๐
def prime_checker(number):
    if n <= 1:
        print("It's not a prime number.")
        return

    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")


# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
