import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = collections.defaultdict(int)
        for char in s:
            frequency[char] += 1
        
        prev_freq = frequency[s[0]]
        for key, value in frequency.items():
            if value != prev_freq:
                return False
        return True
        