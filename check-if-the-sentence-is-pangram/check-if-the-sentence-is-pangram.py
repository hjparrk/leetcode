class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set(sentence)
        return True if len(alphabets) == 26 else False
        