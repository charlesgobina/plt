import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_get_phrase_should_return_phrase(self):
        translator = PigLatin("This is a phrase")
        print(translator.get_phrase())
        self.assertEqual("This is a phrase", translator.get_phrase())

    def test_translate_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.get_phrase())

