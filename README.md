# Project Title: Hangman Project
# Table of contents

1. [Introduction](#introduction)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [What I Have Learned](#what-i-have-learned)
5. [Functions I Used](#functions-i-used)

   
## 1. Introduction <a name="introduction"></a>
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## 2. Installation Instructions <a name="installation-instructions"></a>
In this project, we use GitHub to track changes to our code and save them online in a GitHub repo. 

## 3. Usage Instruction <a name="usage-instructions"></a>
   1. Run Milestone_5.py programme to open the Hangman game app.
   2. Enter the first letter (guess) you want to check using your keyboard.
   3. If you enter character 5 times wrong, you will loose the game.
   4. If guess and enter correct character each time, you will win.
   5. You can enter any particular letter only once.
   6. If there are duplicate letters in the word, you need to enter that letter only once.

## 4. What I Have Learned <a name="what-i-have-learned"></a>
  - use of built-in module random and how to choose a random word from list of words
  - use of functions
  - Use of contional statements and loops
  - use of lists and sets
  - Python coding
  - use of object oriented programming concept
  - use of git and Github
  - use of docstrings

## 5. Functions I Used <a name="functions-i-used"></a>
  - check_guess(guess) - Function to check whether checks if the a particular letter is in the word.. 
  - ask_for_input(): - Function to take an input and validate it as follows.
    - Whether is alphabetic character
    - Whether the length of the input is 1
    - call check_guess() function.
   play_game(word_list) - Function is used to run all code to play the game.
   

                           
