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