from typing import List 
import random
import string


class Hangman:
    def __init__(self,word_list:List[str],num_lives:int = 5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed = ['' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives 
        self.word_list = word_list
        self.list_of_guesses = []
    '''
    Checks the guess provided by the user is valid and if it ends the game by winning or losing
    '''
    def check_guess(self,guess:str)->None:
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index,letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] == letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
    
    '''
    Gets the guess from the user
    '''
    def ask_for_input(self):
        guess = input("Enter a single character ")
        if not(len(guess) == 1 and (guess in string.ascii_lowercase or guess in string.ascii_uppercase)):
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print( "You already tried that letter!")
        else:
            self.check_guess(guess)

def play_game():
    word_list = ['apple','orange','pear','rasberry','lime']
    game = Hangman(word_list=word_list)
    while True:
        if game.num_lives == 0:
            print('you lost!')
            break
        elif game.num_lives < 0:
            raise ValueError('Number of lives cannot be negative')
        elif game.num_lives > 0:
            game.ask_for_input()
        
        if game.num_letters <= 0:
            print("Congratulations! You won.")
            break

if __name__ == '__main__':         
    play_game()

