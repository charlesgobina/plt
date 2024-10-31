
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        words = self.phrase.split()
        if self.phrase.isupper():
            # implement translation for upper case words
            pass
        if len(words) > 1:
            translated_words = []
            for word in words:
                if word[-1].isalpha():
                    translated_words.append(self._translate_single_lowercase_word(word))
                else:
                    clean_word = word[:-1]
                    translated_words.append(self._translate_single_lowercase_word(clean_word) + word[-1])
            return " ".join(translated_words)

        return self._translate_single_lowercase_word(self.phrase)

    def _translate_single_lowercase_word(self, word: str) -> str:
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"

        if '-' in word:
            parts = word.split('-')
            return '-'.join([self._translate_single_lowercase_word(part) for part in parts])

        if word[0] in consonants:
            if all(char in consonants for char in word):
                return word + "ay"
            first_vowel_index = next((i for i, char in enumerate(word) if char in vowels), None)
            if first_vowel_index is None or first_vowel_index == 0:
                return word + "ay"
            return word[first_vowel_index:] + word[:first_vowel_index] + "ay"

        if word.endswith("y"):
            return word + "nay"

        if word[-1] in vowels:
            return word + "yay"

        return word + "ay"

    # implement translation for uppercase words
    def _translate_single_uppercase_word(self, word: str) -> str:
        # logic
        pass


