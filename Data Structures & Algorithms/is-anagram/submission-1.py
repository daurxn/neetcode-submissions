class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurences = {}

        for c in s:
            if c not in occurences:
                occurences[c] = 0
            
            occurences[c] += 1

        for c in t:
            if c not in occurences:
                return False
            
            occurences[c] -= 1

        for value in occurences.values():
            if value != 0:
                return False

        return True