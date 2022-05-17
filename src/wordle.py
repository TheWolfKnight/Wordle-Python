from string import ascii_letters
from random import choice
from time import sleep
from turtle import color


if __name__ == "__main__":
    exit(1)


class InputError(Exception):
    def __init__(self, err_val: chr) -> None:
        self.err_val = err_val

    def __str__(self) -> str:
        return f"The value: {self.err_val} can not be used for this game!"


class WordleGame(object):
    def __init__(self,word_list: list[str], *, guess_amt=6) -> None:
        assert self._validate_word_list(word_list), "Please make sure all words are of equal leangth!"
        self.word: str = None
        self.guess_amt = guess_amt
        self.guesses: list[str] = self._reset_guess_list()
        self.guess: int = 0

    def validate_guess(self, inpt: str) -> bool:
        color_efx: dict[str, str] = {
            "not_in":           "\033[1;31;40m ",
            "in_wrong_place":   "\033[1;33;40m ",
            "in_right_place":   "\033[1;32;40m "
        }
        inpt = inpt.upper()
        if inpt == self.word:
            self._correct_guess(inpt, color_efx["in_right_place"])
            return True
        guess: str = ""
        for idx, val in enumerate(inpt):
            if val not in self.word:
                guess += color_efx["not_in"] + val
            elif val != self.word[idx]:
                guess += color_efx["in_wrong_place"] + val
            else:
                guess += color_efx["in_right_place"] + val
        guess += "\033[0;37;40m"
        self.guesses[self.guess] = guess
        self.guess += 1
        return False

    def get_new_word(self) -> None:
        self.guesses = self._reset_guess_list()
        self.word = choice(self.word_list).upper()
        return

    def validate_input(self, inpt: str) -> bool:
        if len(inpt) != len(self.word):
            print("The input did not match the size of the word!")
            print(f"the word is {len(self.word)} characters long!")
            sleep(2)
            return  False
        for c in inpt:
            if c not in ascii_letters:
                raise InputError(c)
        return True

    def _validate_word_list(self, word_list: list[str]) -> bool:
        target_length: int = len(word_list[0])
        for w in word_list:
            if len(w) != target_length:
                return False
        else:
            self.word_list: list[str] = word_list
            return True

    def _reset_guess_list(self) -> list[str]:
        r: list[str] = []
        self.guess = 0
        for _ in range(self.guess_amt):
            r.append(None)
        return r

    def _correct_guess(self, inpt: str, color_efx: str) -> None:
        guess: str = ""
        for c in inpt:
            guess += color_efx + c
        self.guesses[self.guess] = guess
        return

