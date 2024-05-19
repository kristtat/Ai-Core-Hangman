import random

class Hangman():
    def __init__(self, word_list_of_options, num_lives=5):

        self.word_list_of_options = word_list_of_options
        self.num_lives = num_lives
        self.word_to_guess = random.choice(word_list_of_options)
        self.word_guessed = ['_' for _ in self.word_to_guess]
        self.num_letters = len(set(self.word_to_guess))
        self.word_list_of_options = self.word_list_of_options
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word_to_guess:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
                    
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")  
            print(f"You have {self.num_lives} lives left.")  

    def ask_for_input(self):
        while True:
            guess = input("Please guess one letter below:\n")
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
  

word_list_of_options = ["dragonfruit", "passionfruit", "watermelon", "kiwi", "nectarine"]
hangman = Hangman(word_list_of_options)
hangman.ask_for_input()