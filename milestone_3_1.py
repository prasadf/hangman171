from milestone_2 import word_list,selected_word

while True:
    guess = input('Please guess and enter a single letter: ')
    if (guess.isalpha()):
        if (len(guess)  == 1):
            if (guess in selected_word):
                print(f'Good guess! {guess} is in the word.')
                break
            else:
                print(f'Sorry, {guess} is not in the word. Try again.')
    
            
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
            
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
    
