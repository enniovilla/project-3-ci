import random


def choose_word():
    """
    Function to choose a random word from the list
    """
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'melon']
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Function to display the word with guessed letters and underscores
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            # If the letter has been guessed, show the letter followed by a space
            display += letter + ' '
        else:
            # If the letter hasn't been guessed, show an underscore followed by a space
            display += '_ '
    return display.strip()  # Remove trailing space at the end


def display_hangman(attempts):
    """
    Function to display the hangman based on remaining attempts
    """
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        """
    ]
    
    return stages[attempts]


def hangman():
    """
    Main game function
    """
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print('Welcome to The Hangman Game!')
    print(display_hangman(attempts))
    print(display_word(word, guessed_letters))

    while True:
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            # Check if input is a single letter
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            # Check if the letter has already been guessed
            print('You have already guessed that letter.')
            continue

        guessed_letters.append(guess)

        if guess not in word:
            # If the guessed letter is not in the word, decrement attempts
            attempts -= 1
            if attempts == 0:
                # If no attempts left, end the game
                print("Incorrect! You've run out of attempts. Game over!")
                print(f'The word was: {word}')
                break
            else:
                # Otherwise show the number of attempts remaining
                print(display_hangman(attempts))
                print(f'Incorrect! You have {attempts} attempts left.')
        else:
            print('Correct guess!')

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            # If no underscores left, player wins
            print('You have guessed the word correctly. Congratulations!')
            break


hangman()