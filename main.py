import random

backup_words = [
    "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie",
]  # fmt: skip


def display_title(title_path):
    """Prints the contents of the text file located in the path specified in
    args.

    Args:
        titleFilePath (str): The path of the title text file.
    """
    try:
        with open(title_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(
            "An error occurred while trying to access title file…Exiting application."
        )
        exit()
    except IOError:
        print(
            "An error occurred while trying to fetch the title file...Exiting application."
        )
        exit()


def get_rand_word(words_path, backup_words):
    """Returns a random word from a text file, or a backup list if the file is
    not found.

    Args:
        wordsFilePath (str): The path of the words list file.
        backupWordsList (list): Used if the file path is not found.
    """
    try:
        with open(words_path, "r") as f:
            return random.choice(f.read().split())
    except FileNotFoundError:
        print("Words file not found...backup words will be used instead.")
        return random.choice(backup_words)
    except IOError:
        print(
            "An error occurred while trying to fetch the word...Exiting application."
        )
        exit()


def load_hangman_drawings(drawings_path):
    """Returns a list of hangman drawings from a text file.

    Args:
        hangmanDrawingsFilePath (str): The path of the hangman drawings file.
    """
    try:
        with open(drawings_path, "r") as f:
            return f.read().split("\n\n")
    except FileNotFoundError:
        print(
            "An error occurred while trying to access the hangman drawings file...Exiting application"
        )
        exit()
    except IOError:
        print("An I/O error occurred...Exiting application.")
        exit()


def get_blanked_word(word, guesses):
    """Returns the word to guess with underscores replacing the letters which
    have not been guessed yet.

    Args:
        word (str): The word to guess.
        guesses (list): All guessed letters.
    """
    return (
        "  ".join(letter if letter in guesses else "_" for letter in word)
        + "\n"
    )


def get_guess():
    """Prompts for a guess input and returns it. A list is returned if the
    input is longer than one.
    """
    guess = input("Guess a letter: ").lower()
    while not guess.isalpha():
        guess = input("Please enter only letters of the alphabet: ").lower()
    if len(guess) > 1:
        guess_chars = list(set(guess))
        return guess_chars
    else:
        return guess


def main():
    display_title("hangmanWord.txt")
    print("\n", end="")

    word = get_rand_word("ListOfWords.txt", backup_words)
    guesses = set()
    incorrect_guesses = set()
    correct_guesses_count = 0
    incorrect_guesses_count = 0
    drawings_list = load_hangman_drawings("hangmanDrawings3.txt")
    max_incorrect_guesses = len(drawings_list) - 1

    # ----- Main Game Loop -----
    while True:
        try:
            print(drawings_list[incorrect_guesses_count])
        except IndexError:
            print(f'\nYou lost the game. The correct word was" "{word}"')
            break

        if correct_guesses_count == len(set(word)):
            print("\nWell done...You guessed the word")
            break
        if incorrect_guesses_count == max_incorrect_guesses:
            print(f'\nYou lost the game. The correct word was" "{word}"')
            break

        print(get_blanked_word(word, guesses))
        print(incorrect_guesses or "{}")

        guess = get_guess()
        for char in guess:
            if not char in guesses:
                guesses.update(char)
                if char in list(word):
                    correct_guesses_count += 1
                else:
                    incorrect_guesses.update(char)
                    incorrect_guesses_count += 1


if __name__ == "__main__":
    main()
