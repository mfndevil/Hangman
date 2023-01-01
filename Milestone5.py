# Final hangman game

# Hangman Game

# imports random
import random
# list of words
words = ["pomegranate", "cherry", "mango", "watermelon", "orange"]
print(words)

word = random.choice(words)
print(word)

# sets up hangman class
class Hangman():
    
    # sets up the initialiser and the attributes
    def __init__(self, word_list, num_lives=5):
        self.word = words
        self.word_guessed = ["_"] * len(set(word))
        self.num_letters = len(set(words))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # method to check if the letter guessed is in the word 
    def check_guess(self, guess):
        
        # Checks if input letter is in word, make it lower case
        guess = guess.lower()
        
        if guess in word:
            print(f"Good. {guess} is in the word.")
            for i in range(len(word)):
                 if guess == word[i]:
                    self.word_guessed[i] = guess

            positions = []
            for index, char in enumerate(list(words)):
                if char == guess:
                    positions.append(index)

            return positions

            #  reduces numebr of letters in word by 1        
            self.num_letters -= 1
  
        else:
            # lose 1 life
            self.num_lives -= 1
            print(f"Oops! Incorrect guess!")
            print(f"You have {self.num_lives} lives left")

        # Add guess to the list of guesses
        # self.check_guess(guess)
        self.list_of_guesses += guess

       
    # method to get user input
    def ask_for_input(self):

        while True:
            guess = input("Please enter a single letter: ")

            # checks if the input is valid    
            if guess.isalpha() == False and len(guess) != 1:
                # Print if input is valid
                print("Input is valid")

            # checks if the input has already been tried
            elif guess in self.list_of_guesses:
                print("You've already tried that letter")

            else:
                self.check_guess(guess)
                self.list_of_guesses += guess

            # Call the check guess method then break the loop
            self.check_guess(guess)
            # break

game = Hangman(word_list= words, num_lives= 5)
game.ask_for_input()