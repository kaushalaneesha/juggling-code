class Solution:
    def isPalindrome(self, s:str, start, end) -> bool:
        i = start
        j = end
        while i < j:
            if s[i] == s[j]:
                j -= 1
                i += 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        replaced = False
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j - 1)
        return True
        