from milestone_5 import Hangman

def game_introduction():
    print("Welcome to the Hangman game.")
    print("In this classic game you have to guess the word correctly or you will lose.")
    print("You have unlimited correct guesses but only 5 incorrect guesses...")
    print("But fear not - if you get a letter right, you will win a life back!\n")
    
def play_game(word_list_of_options):
    
    num_lives = 5
    game = Hangman(word_list_of_options, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            repeat_game()
            break

        elif game.num_letters == 0:
            print("Congratulations. You guessed the word correctly and won the game!")
            repeat_game() 
            break  
        
        else:
            print(f"Number of lives left: {game.num_lives}")
            print(f"Number of letters left to guess: {game.num_letters}\n")
            game.ask_for_input()


def repeat_game():
    try:
        user_input = input("Would you like to play again? For 'yes', enter 1. For 'no', enter any other single digit.\n")
        if int(user_input) == 1:
            game_introduction()
            play_game(word_list_of_options)
        else:
            print("Thank you for playing, good bye.")
    except ValueError:
        print("That's not a single digit, let's try that again.") 
        repeat_game()   

if __name__ == "__main__":
    word_list_of_options = ["dragonfruit", "passionfruit", "watermelon", "kiwi", "nectarine"]
    game_introduction()
    play_game(word_list_of_options)

