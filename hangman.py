
import string


#return True if all the letters of secret_word are in letters_guessed False otherwise
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


#return a string of the form 'guessed letters' where the letters in letters_guessed are highlighted with an

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    available_letters = ''
    for letter in string.ascii_uppercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

#runs the hangman game
def hangman(secret_word):
    print('The word is', len(secret_word), 'letters long.')
    letters_guessed = []
    mistakes_made = 0
    while mistakes_made < 8:
        print('You have', 8 - mistakes_made, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ')
        guess = guess.upper()
        if guess in letters_guessed:
            print("\nYou've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print('\nGood guess:', get_guessed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                print('you won!')
                break
        else:
            letters_guessed.append(guess)
            print('\nThat letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            mistakes_made += 1
            if mistakes_made == 8:
                print('you ran out of guesses. The word was', secret_word, '.')
        
#put your "hidden" word in secret_word to play hangman

secret_word = "gass"
hangman(secret_word)     
