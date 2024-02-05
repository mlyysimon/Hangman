import random
from words import words # dataset of words in hangman
import string

def get_valid_word(words):
    word = random.choice(words)
    # make sure words don't have a dash or space
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        # reveal which letters have been guessed
        print(f"\nYou have {lives} lives left and you have used these letters: ", ' '.join(used_letters))

        # reveal current known letters within the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            # tracks which letters have been guessed
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1
                print(f"Letter {user_letter} is not in word.")
                
        elif user_letter in used_letters:
            print("You have already guessed that letter. Please try again.")
            
        else: 
            print("Invalid letter. Please try again.")
    
    if len(word_letters) == 0:
        print(f"Congrats! You guessed the word {word} correctly!")
    else:
        print(f"Sorry, you died. The word was {word}.")

hangman()
    
