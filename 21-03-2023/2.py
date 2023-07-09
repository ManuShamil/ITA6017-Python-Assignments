# 2. Develop the step-by-step program for guessing game using following constraints
#  Note: The player only gets five turns. Hint : use randint( ) function for secret_num
#  The program tells the player after each guess if the number is higher or lower.
#  The program prints appropriate messages for when the player wins and losses.
#  Sample Output:
# Enter your guess (1-100): 50
# LOWER. 4 guesses left.
# Enter your guess (1-100): 25
# LOWER. 3 guesses left.
# Enter your guess (1-100): 12
# LOWER. 2 guesses left.
# Enter your guess (1-100): 6
# HIGHER. 1 guesses left.
# Enter your guess (1-100): 9
# LOWER. 0 guesses left.
# You lose. The correct number is 8

if __name__ == "__main__":
    import random
    secret_num = random.randint(1,100)
    guess = int(input("Enter your guess (1-100): "))
    guess_count = 5
    while guess_count > 0:
        if guess == secret_num:
            print("You win!")
            break
        elif guess < secret_num:
            print("HIGHER. {} guesses left.".format(guess_count-1))
            guess = int(input("Enter your guess (1-100): "))
            guess_count -= 1
        elif guess > secret_num:
            print("LOWER. {} guesses left.".format(guess_count-1))
            guess = int(input("Enter your guess (1-100): "))
            guess_count -= 1
    if guess_count == 0:
        print("You lose. The correct number is {}".format(secret_num))