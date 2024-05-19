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
            self.num_letters -= 1 #decrements per letter, not unique letter
                    
            print(self.word_guessed)
            print(self.num_letters)
                    
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")  
            print(f"You have {self.num_lives} lives left.")  

    def ask_for_input(self):
        while self.num_letters > 0 and self.num_lives > 0:
            print(f"The word you have to guess looks like this: {self.word_guessed}")
            guess = input("Please guess one letter below:\n")
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

