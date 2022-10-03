"""
from hangman import Hangman


def test_display():
    a = Hangman()
    disp = a.display_state()
    assert len(disp) == a.word_len


def test_reveal():
    a = Hangman(force_word="EE")
    a.guess_letter("e")
    a.guess_letter("e")
    assert a.attempts_left == 5


def test_run_out_chances():
    a = Hangman(force_word="Z")
    a.guess_letter("a")
    a.guess_letter("b")
    a.guess_letter("c")
    a.guess_letter("d")
    a.guess_letter("e")
    a.guess_letter("f")
    assert a.attempts_left == 0

    assert a.guess_letter("a") is False
"""
