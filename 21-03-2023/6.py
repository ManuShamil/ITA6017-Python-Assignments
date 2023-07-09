# 6. Program that displays the last digit of a user input number, and also finds out whether 
# the last digit is divisible by 5

n = int(input("Enter a number: "))
last_digit = n % 10

print("Last digit: {}".format(last_digit))
print("Divisible by 5: {}".format(last_digit % 5 == 0))