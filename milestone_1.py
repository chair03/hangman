import random
import string

guess = input("Enter a single character ")

if len(guess) == 1 and (guess in string.ascii_lowercase or guess in string.ascii_uppercase):
    print('Good guess!')
else:
    print("Oops! That is not a valid input.")

word_list = ['apple','orange','pear','rasberry','lime']
word = random.choice(word_list)
print(word)