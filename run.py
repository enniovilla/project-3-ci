import random
from colorama import Fore, Back, Style


def choose_word(category):
    """
    Dictionary containing words for each category
    """
    word_dict = {
        1: ['leopard', 'turtle', 'rabbit', 'elephant', 'giraffe', 'tiger'],
        2: ['soccer', 'basketball', 'tennis', 'swimming',
            'snowboarding', 'boxing'],
        3: ['pizza', 'hamburger', 'sushi', 'pasta', 'steak', 'salad'],
        4: ['coffee', 'milkshake', 'juice', 'lemonade', 'water', 'smoothie'],
        5: ['guitar', 'piano', 'violin', 'trumpet', 'drums', 'flute'],
        6: ['brown', 'white', 'green', 'yellow', 'orange', 'purple'],
        7: ['apple', 'banana', 'orange', 'grape', 'strawberry', 'melon'],
        8: ['doctor', 'engineer', 'teacher', 'artist', 'nurse', 'scientist']
    }

    return random.choice(word_dict[category])


def display_word(word, guessed_letters):
    """
    Function to display the word with guessed letters and underscores
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            """
            If the letter has been guessed,
            show the letter followed by a space
            """
            display += letter + ' '
        else:
            """
            If the letter hasn't been guessed,
            show an underscore followed by a space
            """
            display += '_ '
    return display.strip()  # Remove trailing space at the end


def display_hangman(attempts):
    """
    Function to display the hangman based on remaining attempts
    """
    stages = [
        r"""
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
        """,
        r"""
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     /
        """,
        r"""
           --------
           |      |
           |      O
           |     \|/
           |      |
           |
        """,
        r"""
           --------
           |      |
           |      O
           |     \|
           |      |
           |
        """,
        r"""
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        r"""
           --------
           |      |
           |      O
           |
           |
           |
        """,
        r"""
           --------
           |      |
           |
           |
           |
           |
        """
    ]

    if attempts >= 1:
        # Adjusted index to match attempts left
        return stages[attempts-1]
    else:
        return stages[0]


def hangman():
    """
    Main game function
    """
    # List of tuples containing categories and their corresponding names
    categories = [
        (1, 'Animal'),
        (2, 'Sport'),
        (3, 'Food'),
        (4, 'Drink'),
        (5, 'Musical Instrument'),
        (6, 'Color'),
        (7, 'Fruit'),
        (8, 'Profession')
    ]

    # Prompt player to choose a category
    print('Choose a category to play:')
    for category in categories:
        print(f'{category[0]}. {category[1]}')

    while True:
        category_choice = input(
            'Enter the number corresponding to the category: '
            )

        # Validate category choice
        valid_choices = [str(category[0]) for category in categories]
        if category_choice not in valid_choices:
            print('\nInvalid category choice. ')
            continue

        category_choice = int(category_choice)
        break

    word = choose_word(category_choice)
    guessed_letters = []
    attempts = 6

    print(Back.GREEN + "\nLet's play!" + Back.RESET)
    print(display_hangman(attempts))
    # Adjust index for category choice
    print('\nCategory: '
          f'{Fore.YELLOW}{categories[category_choice-1][1]}{Fore.RESET}')
    print(display_word(word, guessed_letters))

    while True:
        try:
            guess = input('\nGuess a letter: ').lower()

            if len(guess) != 1 or not guess.isalpha():
                # Check if input is a single letter
                print(Fore.CYAN + 'Please enter a single letter.' + Fore.RESET)
                continue

            if guess in guessed_letters:
                # Check if the letter has already been guessed
                print(Fore.CYAN +
                "You've already guessed that letter." +
                Fore.RESET)
                continue

            guessed_letters.append(guess)

            if guess not in word:
                # If the guessed letter is not in the word, decrement attempts
                attempts -= 1
                if attempts == 0:
                    # If no attempts left, end the game
                    print(f'{Fore.RED}Incorrect!{Fore.RESET} '
                          "You've run out of attempts. "
                          f"{Back.RED}Game over!{Back.RESET}")
                    print(f'The word was: {Fore.YELLOW}{word}{Fore.RESET}')
                    break
                else:
                    print(display_hangman(attempts))
                    print(f'{Fore.RED}Incorrect!{Fore.RESET} '
                          f'You have {Fore.YELLOW}{attempts}{Fore.RESET}'
                          ' attempts left.\n')
            else:
                print(Fore.GREEN + '\nCorrect guess!\n' + Fore.RESET)

            display = display_word(word, guessed_letters)
            print(display)

            if "_" not in display:
                # If no underscores left, player wins
                print(Back.GREEN +
                "Congratulations! You've guessed the word correctly!" +
                Back.RESET)
                break
        except KeyboardInterrupt:
            print("\n\nExiting the game.")
            break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    # Ask if the player wants to play again
    while True:
        play_again = input('Would you like to play again? (yes/no): ').lower()
        if play_again == 'yes' or play_again == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")

    if play_again == 'yes':
        print('\n')
        hangman()
    else:
        print(Fore.YELLOW + '\nThank you for playing!' + Fore.RESET)


print(Fore.YELLOW + 'Welcome to The Hangman Game!\n' + Fore.RESET)
hangman()
