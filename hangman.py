import json
import random

WORDS_FILE = "words.txt"
HISTORY_FILE = "game_history.json"

MAX_WRONG_ATTEMPTS = 7

HANGMAN_STAGES = (
    """
      _______
      |     |
      |
      |
      |
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |
      |
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |     |
      |
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|
      |
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |    /
      |
    __|__
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |    / \\
      |
    __|__
    """,
)

def load_words(file_path):
    try:
        with open(file_path, "r") as file:
            words = [line.strip().lower() for line in file if line.strip()]
        return words
    except Exception:
        return []

def load_history(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_history(file_path, history):
    try:
        with open(file_path, "w") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)
    except Exception:
        print("Error saving history.")

def choose_word(words):
    return random.choice(words)

def show_hangman(wrong):
    print(HANGMAN_STAGES[min(wrong, len(HANGMAN_STAGES) - 1)])

def mask_word(secret_word, guessed):
    return " ".join(
        [letter if letter in guessed else "_" for letter in secret_word]
    )

def is_solved(secret_word, guessed):
    for letter in secret_word:
        if letter not in guessed:
            return False
    return True

def get_guess(used_letters):
    while True:
        guess = input("Enter a letter or word: ").lower().strip()

        if not guess:
            print("Empty input.")
        elif not guess.isalpha():
            print("Only letters are allowed!")
        elif len(guess) == 1 and guess in used_letters:
            print("This letter was already used.")
        else:
            return guess

def play(words, history):
    secret_word = choose_word(words)

    guessed = set()
    wrong_letters = set()
    wrong_attempts = 0

    print("I have chosen a word!")

    while (
        wrong_attempts < MAX_WRONG_ATTEMPTS
        and not is_solved(secret_word, guessed)
    ):

        print("Word:", mask_word(secret_word, guessed))

        print(
            "Used letters:",
            ", ".join(guessed | wrong_letters)
            if guessed or wrong_letters
            else "none"
        )

        show_hangman(wrong_attempts)

        guess = get_guess(guessed | wrong_letters)

        if len(guess) > 1:
            if guess == secret_word:
                guessed.update(secret_word)
            else:
                wrong_attempts += 1
                print("Incorrect word.")

        else:
            if guess in secret_word:
                guessed.add(guess)
                print("Correct!")
            else:
                wrong_attempts += 1
                wrong_letters.add(guess)
                print("Incorrect.")

    if is_solved(secret_word, guessed):
        print("You won! The word was:", secret_word)
        result = "win"
    else:
        print("You lost. The word was:", secret_word)
        show_hangman(wrong_attempts)
        result = "lose"

    game_record = {
        "word": secret_word,
        "result": result,
        "wrong_attempts": wrong_attempts,
        "letters": list(guessed | wrong_letters)
    }

    history.append(game_record)

    save_history(HISTORY_FILE, history)

def show_history(history):
    if not history:
        print("History is empty.")
        return

    print("Game history:")

    for i, game in enumerate(history, 1):
        print(
            f"{i}. Word: {game['word']} | "
            f"Result: {game['result']} | "
            f"Attempts: {game['wrong_attempts']}"
        )

def main():
    words = load_words(WORDS_FILE)
    history = load_history(HISTORY_FILE)

    if not words:
        print("No words found in words.txt")
        return

    while True:
        print("\n1 - Play")
        print("2 - History")
        print("3 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            play(words, history)

        elif choice == "2":
            show_history(history)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Critical error:", e)