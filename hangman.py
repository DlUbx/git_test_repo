import random

# ASCII Art for Hangman (for wrong guesses)
HANGMAN_PICS = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    '''
]

def print_hangman(tries):
    print(HANGMAN_PICS[tries])

def play_hangman(word):
    word = word.lower()
    guessed = ["_"] * len(word)
    guessed_letters = set()
    tries = 6

    while tries > 0:
        print(f"Word to guess: {' '.join(guessed)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print_hangman(tries)

        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        if "_" not in guessed:
            print(f"Congratulations! You've guessed the word: {''.join(guessed)}")
            break
    else:
        print_hangman(tries)
        print(f"You've run out of tries! The word was: {word}")

if __name__ == "__main__":
    word = input("Enter the word to guess: ").lower()
    play_hangman(word)
