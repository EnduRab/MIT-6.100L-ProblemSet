# Problem Set 2, hangman.py
# Name: QUI
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    letters = letters_guessed[:]
    for word in secret_word:
      if word not in letters:
        return False
    return True
    


def get_word_progress(secret_word, letters_guessed):
    curr = list("*" * len(secret_word))
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            curr[i] = secret_word[i]
    return ''.join(curr)    


def get_available_letters(letters_guessed):
    available_letters = string.ascii_lowercase
    for word in letters_guessed:
        available_letters = available_letters.replace(word,"")
    return available_letters

def help(secret_word, letters_guessed):
    available_letters = get_available_letters(letters_guessed)
    choose_from = ""
    for word in secret_word:
       if word in available_letters:
          choose_from += word
    new = random.randint(0,len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def hangman(secret_word, with_help):
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses = 10
    vowels = ['a','o','e','u','i']

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    while guesses > 0:

      print_statements(guesses,letters_guessed)
      player_guess = input("Please guess a letter: ").lower()

      if with_help == True and player_guess == '!':
        if guesses < 3:
           print("Oops! Not enough guesses left: ", end="")
        else:
           reveal = help(secret_word,letters_guessed)
           print(f"Letter revealed: {reveal}", )
           letters_guessed.append(reveal)
           guesses -= 3
      elif len(player_guess) != 1 or not player_guess.isalpha():

        print("Oops! That is not a valid letter. Please input a letter from the alphabet: ", end="")

      else:

        if player_guess in letters_guessed:

          print("Oops! You've already guesses that letter: ", end='')

        else:

          letters_guessed.append(player_guess)

          if player_guess in secret_word:
            print("Good guess: ", end='')

          else:
              print("Oops! That letter is not in my word: ", end='')
              if player_guess in vowels:
                guesses -= 2

              else:
                guesses -= 1

      print(get_word_progress(secret_word,letters_guessed))
      if(has_player_won(secret_word,letters_guessed)):
         total_score = calculate_score(secret_word,guesses)
         print("------------------")
         print("Congratulations, you won!")
         print("Your total score for this game is:",total_score)
         break
    if(guesses <= 0 and not has_player_won(secret_word,letters_guessed)):
      print("------------------")
      print(f"Sorry, you ran out of guesses. The word was {secret_word}.", )

def calculate_score(secret_word, guesses):
   unique_letter = len(set(secret_word))
   total_score = (guesses + 4 * unique_letter) + 3 * len(secret_word)
   return total_score

         

def print_statements(guesses,letters_guessed):
    print("----------------")
    print(f"You have {guesses} guesses left.")
    print("Available letters: ", get_available_letters(letters_guessed))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)
  