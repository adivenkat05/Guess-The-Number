import random

# range of number
top_of_range = input("Enter range of number: ")

# if top_of range is a digit it'll type cast it to integer.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

# if top_of_range is 0 smaller than 0.
    if top_of_range <= 0:
        print("Please enter a number larger than 0.")

# Type a number next time if it's not digit.
else:
    print("PLEASE TYPE A NUMBER NEXT TIME.")

# randint(0, range) will generate a random number until given range.
random_number = random.randint(0, top_of_range)

while True:
    # Taking input from user.
    user_guess = input("Make a guess: ")

    # if user_guess is digit it'll typecast it to integer.
    if user_guess.isdigit():
        user_guess = int(user_guess)

    # else loop will executed once again until numguess = 0ber is given.
    else:
        print("PLEASE TYPE A NUMBER NEXT TIME.")
        continue

    # if user_guess is same as random_number
    if user_guess == random_number:
        print("WHOAHH!! YOU'VE GUESSED IT RIGHT !!!")
        quit()  # quit() will end the loop.

    # if user_guess is lower than random_number.
    elif user_guess < random_number:
        print("Too Low.\n")

    # if user_guess is higher than random_number.
    elif user_guess > random_number:
        print("Too High.\n")
