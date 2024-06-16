class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j] >= '1' and abbr[j] <= '9': # Number 
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num*10+int(abbr[j])
                    j+=1
                i += num
            elif abbr[j] != word[i]:
                return False
            else:
                i += 1
                j += 1
        
        if i == len(word) and j == len(abbr):
            return True
            
             

        