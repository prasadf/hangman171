import random
# list of different fruits
word_list = ['banana','orange','mango','apple','grapes']

print(word_list)

# function to choose a random friut from word_list
def choice(word_list):
    word = random.choice(word_list)
    return word

print(f'Random choice fruit is: {choice(word_list)}')
# user input single letter
guess = input('Please enter a single letter: ')
# check whether the user input is validls

if len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! This is not a valid input.')
print(guess)