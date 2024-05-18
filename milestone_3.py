import random

word_list_of_options = ["dragonfruit", "passionfruit", "watermelon", "kiwi", "nectarine"]
word_to_guess = random.choice(word_list_of_options)


def check_guess(guess):
    guess = guess.lower()
    if guess in word_to_guess:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please guess one letter below:\n")
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)    

ask_for_input()

