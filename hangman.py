import random
import string

WORDLIST_FILENAME = "words.txt"


#def load_words():
   # '''return a list of valid words'''
    #words = []
   # with open(WORDLIST_FILENAME, 'r') as f:
       # for line in f:
            #words.append(line.strip())
   # return words
   


def is_word_guessed(secret_word, letters_guessed):
    '''return True if all the letters of secret_word are in letters_guessed;
    False otherwise'''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''return a string of the form 'guessed letters' where the letters in
    letters_guessed are highlighted with an '_' '''
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''return a string of letters that are not yet guessed'''
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

#runs the hangman game
def hangman(secret_word):
    print('hangmannn')
    print('The word is', len(secret_word), 'letters long.')
    print('-------------')
    letters_guessed = []
    mistakes_made = 0
    while mistakes_made < 8:
        print('You have', 8 - mistakes_made, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            print('-------------')
        elif guess in secret_word:
            letters_guessed.append(guess)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            print('-------------')
            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won!')
                break
        else:
            letters_guessed.append(guess)
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            print('-------------')
            mistakes_made += 1
            if mistakes_made == 8:
                print('Sorry, you ran out of guesses. The word was', secret_word, '.')
        
#put your word here to play the game        
hangman("")