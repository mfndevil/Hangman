import random

'list of words'
word_list = ["mangoes", "pomegranates", "strawberry", "oranges", "pineapples"]
word = random.choice(word_list)

print(word)

'While loop to run continuously'
while True:
    'gets user input'
    guess = input("Please enter a single letter: ")

    'checks if input is valid'
    if guess.isalpha() and len(guess) == 1:
        'Print if input is valid'
        print("Input is valid")
        
    else:
        'Print if input is not valid'
        print("Oops. Invalid input. Please enter a single alpabet")
        

    'Checks if input letter is in word'
    if guess in word:
        print(f"Good. {guess} is in the word.")
    else:
        print("Oops! Incorrect guess!")