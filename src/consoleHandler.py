
from subprocess import run


if __name__ == "__main__":
    exit(1)


class ConsoleHandler(object):
    def __init__(self) -> None:
        self.clear_console()

    def clear_console(self) -> None:
        run(['cls'], shell=True, capture_output=False)

    def print_guesses(self, word_length: int=None, guess_list: list[str]=None, num_loop: int=0) -> None:
        loop_over = guess_list if guess_list else range(num_loop)
        for guess in loop_over:
            if isinstance(guess, int) or not guess:
                self._print_blank_word(word_length)
                continue
            print(guess)
        print("\033[0;37;40m")
        return

    def _print_blank_word(self, length_word: int) -> None:
        s: str = "_" * length_word
        print(s)

