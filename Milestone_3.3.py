import random
# list of words
word_list = ["mangoes", "pomegranates", "strawberry", "oranges", "pineapples"]
word = random.choice(word_list)
print(word)

def check_guess(guess):
    # checks if input is valid 
    if guess.isalpha() and len(guess) == 1:
        # Print if input is valid
        print("Input is valid")
    
    else:
        # Print if input is not valid
        print("Oops. Invalid input. Please enter a single alpabet")
    

    # Checks if input letter is in word and makes it lower case
    if guess in word:
        print(f"Good. {guess.lower()} is in the word.")
    else:
        print("Oops! Incorrect guess!")

def ask_for_input():
    # gets user input and checks if the guess is valid
    while True:
        guess = input("Please enter a single letter: ")
            
        check_guess(guess)    
        
ask_for_input()