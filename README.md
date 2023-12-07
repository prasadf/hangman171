# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### What I have learned
  - use of built-in module random
  - how to choose a random word from list of words
  - use of input() function
  - use of if - else to validate user input

## Functions I used
  - def check_guess(guess) - Function to check whether the guessed character is in the random word.
  - def ask_for_input(): - Function to take an input and validate it as follows.
    - Whether is alphabetic character
    - Whether the length of the input is 1
    - call check_guess() function.
                           
