import random

word_list = ["dragonfruit", "passionfruit", "watermelon", "kiwi", "nectarine"]
print(word_list)


word = random.choice(word_list)
print(word)

guess = input("Please enter one letter for your guess below:\n")

if len(guess) == 1 and type(guess) == str:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
