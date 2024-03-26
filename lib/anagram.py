# your code goes here!
class Anagram:
    def __init__(self, word):
        self._word = word
    @property
    def word(self):
        return self._word
    
    @word.setter
    def set_word(self, word):
        self._word = word

    def match(self, anagrams):
       matched_anagrams = []
       sorted_word  = sorted(self._word.lower())
       for anagram in anagrams:
            sorted_anagram = sorted(anagram.lower())
            if sorted_word == sorted_anagram and self._word.lower() != anagram.lower():
               matched_anagrams.append(anagram)
            else:
               return matched_anagrams