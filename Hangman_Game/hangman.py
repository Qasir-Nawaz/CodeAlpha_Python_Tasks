"""
Hangman Game - CodeAlpha Python Internship Task 1
Author: Qasir Nawaz
"""

import random

WORDS = ["python", "coding", "hangman", "computer", "internship"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]


def display_board(wrong_guesses, guessed_letters, word):
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display_word}\n")


def play_hangman():
    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME!")
    print("=" * 40)

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < 6:
        display_board(wrong_guesses, guessed_letters, word)

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print(f"⚠  You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.\n")

    else:
        display_board(wrong_guesses, guessed_letters, word)
        print(f"💀 Game Over! The word was: '{word.upper()}'")

    play_again = input("\nPlay again? (yes/no): ").lower().strip()
    if play_again == "yes":
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye! 👋")


if __name__ == "__main__":
    play_hangman()