# 8. Program that finds whether a user given value is divisible by 3, 4 and both.

n = int(input("Enter a number: "))
print("Divisible by 3: {}".format(n % 3 == 0))
print("Divisible by 4: {}".format(n % 4 == 0))
print("Divisible by 3 and 4: {}".format(n % 3 == 0 and n % 4 == 0))