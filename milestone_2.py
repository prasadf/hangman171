import random
# list of different fruits
word_list = ['banana','orange','mango','apple','grapes']

print(word_list)

# function to choose a random friut from word_list
def choice(word_list):
    selected_word = random.choice(word_list)
    return selected_word

selected_word = choice(word_list)
print(f'Random choice fruit is: {choice(word_list)}')
# user input single letter
guess_letter = input('Please enter a single letter: ')
# check whether the user input is validls

if len(guess_letter) == 1:
    print('Good guess!')
else:
    print('Oops! This is not a valid input.')
print(guess_letter)