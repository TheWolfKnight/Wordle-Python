
from src import WordleGame, ConsoleHandler, InputError

from typing import Optional, Union
from time import sleep
from json import loads
from sys import argv


USE_PREDEFINED_WORDS: bool = True
CONST_PREDEFINED_WORD_LENGTHS: list[int] = ["5"]


def read_word_list(word_lengt: str="5", word_list_path: str="./src/wordList.json") -> list[str]:
    with open("./src/wordList.json", 'r') as fp:
        words: list[str] = loads(fp.read())[word_lengt]
    return words


def next_argv(argv: list[str]) -> Union[str, Optional[list[str]]]:
    return argv[0], argv[1:]


def main(argv: list[str]) -> int:
    global USE_PREDEFINED_WORDS, CONST_PREDEFINED_WORD_LENGTHS

    word_len: str = "5"
    word_list_path: str = "./src/wordList.json"

    while argv:
        com, argv = next_argv(argv)
        if com in ("--word_len", "-w"):
            word_len, argv = next_argv(argv)
            if word_len not in CONST_PREDEFINED_WORD_LENGTHS: USE_PREDEFINED_WORDS = False
        elif com in ("--wordlist_path", "-p"):
            word_list_path, argv = next_argv(argv)

    word_list: list[str] = read_word_list(word_lengt=word_len, word_list_path=word_list_path)

    game: WordleGame = WordleGame(word_list)
    consoleHandl: ConsoleHandler = ConsoleHandler()

    get_new_word: bool = True

    while True:
        if get_new_word:
            game.get_new_word()
            get_new_word = False
        consoleHandl.print_guesses(word_length=len(game.word_list[0]), guess_list=game.guesses)
        user_inpt: str = input("Make A Guess > ")
        try:
            is_valid: bool = game.validate_input(user_inpt)
        except InputError as e:
            print(e)
            sleep(3.5)
            continue

        consoleHandl.clear_console()

        if not is_valid:
            continue

        if game.validate_guess(user_inpt) or game.guess == len(game.guesses):
            print(f"The word was {game.word}")
            print("Do you want to play again?")
            if input("[Y|n] > ") not in "Yy":
                break
            get_new_word = True

    return 0


if __name__ == "__main__":
    try:
        return_code: int = main(argv)
        exit(return_code)
    except KeyboardInterrupt:
        print("\nExiting game")
        exit(1)

