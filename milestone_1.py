import random

'list of words'
word_list = ["Mangoes", "Pomegranates", "Passion Fruits", "Oranges", "Pineapples"]
random.choice(word_list)

'print the list above'
print(random.choice(word_list))

'take user input'
guess = input("Please enter a word or letter: ")
##aprint(len(guess))

'check the length of the user input and if input is an alphabet'
if guess.isalpha() and len(guess) == 1:
    print("Good guess")

##if guess >= "a" and guess <= "z":
    ##1print("Good guess!")
    
else:
    print("Ooops! Invalid input. Try again.")
