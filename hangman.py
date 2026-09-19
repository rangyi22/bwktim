"""Simple cross-platform Hangman game."""
from __future__ import annotations

import random
import string
from typing import Iterable, Sequence

DEFAULT_WORDS: Sequence[str] = (
    "python",
    "hangman",
    "developer",
    "keyboard",
    "function",
    "variable",
    "algorithm",
    "terminal",
    "debugging",
    "iteration",
)

HANGMAN_STAGES: Sequence[str] = (
    """
     +---+
         |
         |
         |
        ===
    """.strip("\n"),
    """
     +---+
     O   |
         |
         |
        ===
    """.strip("\n"),
    """
     +---+
     O   |
     |   |
         |
        ===
    """.strip("\n"),
    """
     +---+
     O   |
    /|   |
         |
        ===
    """.strip("\n"),
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """.strip("\n"),
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """.strip("\n"),
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """.strip("\n"),
)


def choose_word(words: Iterable[str]) -> str:
    """Choose a word from the provided iterable."""
    word_list = [word.strip().lower() for word in words if word.strip()]
    if not word_list:
        raise ValueError("word list is empty")
    return random.choice(word_list)


def format_progress(word: str, guesses: set[str]) -> str:
    """Return the display string showing guessed letters."""
    return " ".join(letter if letter in guesses else "_" for letter in word)


def is_word_guessed(word: str, guesses: set[str]) -> bool:
    """Check whether all letters in the word have been guessed."""
    return set(word).issubset(guesses)


def prompt_for_guess(guessed_letters: set[str]) -> str:
    """Prompt the player for a single, new letter guess."""
    while True:
        raw_guess = input("Guess a letter: ").strip().lower()
        if len(raw_guess) != 1 or raw_guess not in string.ascii_lowercase:
            print("Please enter a single letter (a-z).")
            continue
        if raw_guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue
        return raw_guess


def play_hangman(words: Sequence[str] = DEFAULT_WORDS, max_wrong: int | None = None) -> bool:
    """Run a single game of hangman. Returns True if the player wins."""
    word = choose_word(words)
    wrong_guesses = 0
    guessed_letters: set[str] = set()
    allowed_wrong = max_wrong if max_wrong is not None else len(HANGMAN_STAGES) - 1
    allowed_wrong = min(allowed_wrong, len(HANGMAN_STAGES) - 1)

    print("\nWelcome to Hangman!\n")

    while wrong_guesses <= allowed_wrong:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {format_progress(word, guessed_letters)}")
        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Remaining mistakes: {allowed_wrong - wrong_guesses}\n")

        if is_word_guessed(word, guessed_letters):
            print(f"You win! The word was '{word}'.")
            return True

        guess = prompt_for_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Nope, that letter is not in the word.\n")
        else:
            print("Nice! That letter is in the word.\n")

        if is_word_guessed(word, guessed_letters):
            print(f"You win! The word was '{word}'.")
            return True

    print(HANGMAN_STAGES[-1])
    print(f"Game over! The word was '{word}'.")
    return False


def main() -> None:
    """Entry point for the command-line game."""
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
