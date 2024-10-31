class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        
        if self.phrase[0] in consonants:
            if all(char in consonants for char in self.phrase):
                return self.phrase + "ay"
            first_vowel_index = next((i for i, char in enumerate(self.phrase) if char in vowels), None)
            if first_vowel_index is None or first_vowel_index == 0:
                return self.phrase + "ay"
            return self.phrase[first_vowel_index:] + self.phrase[:first_vowel_index] + "ay"
        
        if self.phrase.endswith("y"):
            return self.phrase + "nay"
        
        if self.phrase[-1] in vowels:
            return self.phrase + "yay"
        
        return self.phrase + "ay"

