class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if abbr[j] != word[i]:
                    return False
                else:
                    i += 1
                    j += 1
                    continue
            num = 0
            if abbr[j] == '0':
                return False
            while j < len(abbr) and abbr[j].isdigit():
                num = num*10+int(abbr[j])
                j+=1
            i += num
        if i == len(word) and j == len(abbr):
            return True
        return False
            
             

        