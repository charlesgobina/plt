import unittest
from fnmatch import translate

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_get_phrase_should_return_phrase(self):
        translator = PigLatin("This is a phrase")
        print(translator.get_phrase())
        self.assertEqual("This is a phrase", translator.get_phrase())

    def test_translate_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_translate_word_ending_with_y(self):
        translator = PigLatin("any")
        # append "nay" to words ending with y
        self.assertEqual("anynay", translator.translate())

    def test_translate_word_ending_with_vowel(self):
        translator = PigLatin("apple")
        # for words ending with vowels, append "yay" to the end of the word
        self.assertEqual("appleyay", translator.translate())

    def test_translate_word_ending_with_consonant(self):
        translator = PigLatin("ask")
        # for words ending with consonant, append "ay" to the end of the word
        self.assertEqual("askay", translator.translate())



