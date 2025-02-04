# O(N) Time and Space Complexity
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ensure case-insensitive
        s = s.lower()
        t = t.lower()

        #check same length
        if len(s) != len(t):
            return False

        #use hashing to know when frequency of char does/ doesn't follow'
        hashmap = Counter(s)
        for char in t:
            if hashmap[char] == 0:
                return False
            hashmap[char]-=1

        return True
