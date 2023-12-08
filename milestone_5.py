import random

# class definition
class Hangman:
    '''
    This class is used to develop Hangman game.
    Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. 
    This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

    '''

    # class constructor
    def __init__(self, word_list, num_lives = 5):
        '''
        This function is used to initialise the Hangman class constructor.

        Parameters:
            word_list (list): A list of words
            num_lives (int): The number of lives the player has at the start of the game.
    
        Attributes:
        word (str): The word to be guessed, picked randomly from the word list.
        word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed. 
        num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
        list_of_guesses (list):  list of the guesses that have already been tried.
        '''
        
        # class atributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    # function to check whether guessed charcter is in the random word selected.
    def check_guess(self, guess):
        '''
            This function is used to check if the guessed letter is in the word.

            Parameter:
                guess (str): Gueseed letter to be checked

       '''
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
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left')
            
    # function to take input from the user and validate it.
    def ask_for_input(self):
        '''
        This function is used to asks the user for a letter to be checked.

        Parameters: None
        '''
        while True:
            # Ask for user input
            guess = input('Please enter a letter: ')
           # validate whether the input is alphabetical single lettergit add
            if (not (guess.isalpha() and (len(guess) == 1))):
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
def play_game(word_list):
    '''
    This function is used to run all code to play the game.

    Parameter:
        word_list (list): List of words to be used in the game.

    '''
    num_lives = 5
    # create new instance of Hangman class
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost.')
            break
        if (game.num_letters > 0):
            game.ask_for_input()
        if (game.num_lives != 0) and (game.num_letters <= 0):
            print('Congratulations. You won the game!')
            break

word_list = ['apple', 'banana', 'mango', 'orange', 'grapes']
play_game(word_list )
    
