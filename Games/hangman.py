"""
Hangman exercise
H_LLO

1/
Create a game
Start it by picking a random word from
    norvig.com/ngrams/sowpods.txt
Create a function to display current state

2/
Allow user to guess a letter, and
Validate the input
Display the result (new revealed letters, or write out “not in word!”)

3/
Keep track of the allowed guesses (start with 6)
Decrement for each new guess (do not penalize for guessing the same letter twice)
Display the remaining allowed guesses at each turn (ie You have 5 guesses remaining)

4/
Have a new game option
Display the hangman to symbolize the number of guesses

/

/ \

 |
/ \

-|
/ \

-|-
/ \

 o
-|-
/ \

"""

import random

"""
class Hangman:

    def __init__(self, force_word: str = ""):
        if force_word != "":
            self.word = force_word
        else:
            self.word = Hangman.get_word()
        self.attempts_left = 6
        self.word_len = len(self.word)
        self.revealed = [0] * self.word_len

        self.guessed = set()

    def display_state(self, display_all=False):
        to_display = ""
        for idx in range(self.word_len):
            if (self.revealed[idx] == 1) or display_all:
                to_display += self.word[idx]
            else:
                to_display += "_"
        return to_display

    def guess_letter(self, letter):
        if self.attempts_left <= 0:
            print("No more attempts, you lose")
            return False
        is_valid, clean = Hangman.validate_letter(letter)
        if not is_valid:
            print("Please enter a valid string, you entered %s" % letter)
            return False

        # If invalid we do not count as error
        revealed = 0

        for idx in range(self.word_len):
            if self.word[idx] == clean:
                self.revealed[idx] = 1
                revealed += 1

        if revealed == 0:
            print("letter not in word")
            self.attempts_left -= 1
        else:
            if clean not in self.guessed:
                self.guessed.add(clean)
                self.attempts_left -= 1
        if self.attempts_left <= 0:
            print("No more attempts, you lose")
            print("The word was %s" % self.display_state(True))
        else:
            print("%s attempts left" % self.attempts_left)
        print(self.display_state())

    def start_game_loop(self):
        print(self.display_state())
        while self.attempts_left > 0:
            clean = Hangman.get_letter()
            self.guess_letter(clean)

    @staticmethod
    def get_word():
        with open('sowpods.txt') as f:
            words = f.read()
        word_list = words.split('\n')
        return random.choice(word_list)

    @staticmethod
    def validate_letter(letter):
        if not isinstance(letter, str):
            return False, ""
        if len(letter) != 1:
            return False, ""
        uppercase = str.upper(letter)
        if uppercase.isalpha():
            return True, uppercase

    @staticmethod
    def get_letter(check_new_game=False):
        letter_valid = False
        while not letter_valid:
            raw = input("Please enter a letter")
            letter_valid, clean = Hangman.validate_letter(raw)
            if check_new_game and letter_valid:
                letter_valid = clean in ["Y", "N"]
        return clean

    @staticmethod
    def start_session_loop():
        print("Would you like to play? y for yes, n for no")
        want_to_play = Hangman.get_letter(check_new_game=True)
        while want_to_play == "Y":
            game = Hangman()
            game.start_game_loop()
            print("Would you like to play? y for yes, n for no")
            want_to_play = Hangman.get_letter(check_new_game=True)


if __name__ == '__main__':
    a = Hangman()
    a.start_session_loop()
"""
