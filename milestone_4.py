import random

# class definition
class Hangman:

    # class constructor
    def __init__(self, word_list, num_lives = 5):
        # class atributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word_guessed))
        self.list_of_guesses = []

    # function to check whether guessed charcter is in the random word selected.
    def check_guess(self, guess):
        # convert input to lower case
        guess = guess.lower()
        # check whether guessed word is in the word selected.
        if (guess in self.word):
            print(f'Good guess! {guess} is in the word.')
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(guess)] = guess
                    break
            self.num_letters -= 1
        else:
            # guess is not in the word.
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in theword.')
            print(f'You have {self.num_lives} lives left')
            
    # function to take input from the user and validate it.
    def ask_for_input(self):
        # print(self.word)
        while True:
            # Ask for user input
            guess = input('Please guess a letter and enter: ')
           # validate whether the input is alphabetical single lettergit add
            if (not (guess.isalpha() and (len(guess) == 1))):
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

Hangman1 = Hangman(['apple', 'banana', 'mango', 'orange', 'grapes'],5)
Hangman1.ask_for_input()
    
