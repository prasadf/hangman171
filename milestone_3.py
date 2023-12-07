import random
# list of different fruits
word_list = ['banana','orange','mango','apple','grapes']


print(word_list)

# function to choose a random friut from word_list
def choice(word_list):
    selected_word = random.choice(word_list)
    return selected_word

selected_word = choice(word_list)
print(f'Random choice fruit is: {selected_word}')
# user input single letter
#guess_letter = input('Please enter a single letter: ')
# check whether the user input is validls

# Function to check selected character is in the random word.
def check_guess(guess):
    # Converts guess variable to lowercase
    guess = guess.lower()
    # Check whether given character is inside the selected word
    if (guess in selected_word):
        print(f'Good guess! {guess} is in the word.')
        
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
        
        
# Function to take input and check for validity
def ask_for_input():

    while True:
        guess = input('Please guess and enter a single letter: ')
        if (guess.isalpha()):
            if (len(guess)  == 1):
                check_guess(guess)
                break
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
            
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

ask_for_input()
