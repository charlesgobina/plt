class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        if self.phrase[0] not in "aeiou":
            return self.phrase[1:] + self.phrase[0] + "ay"
        if self.phrase.endswith("y"):
            return self.phrase + "nay"
        if self.phrase[-1] in "aeiou":
            return self.phrase + "yay"
        return self.phrase + "ay"

