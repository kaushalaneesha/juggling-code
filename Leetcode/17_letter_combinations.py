from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return 
            
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        def helper(index, curr_comm):
            if index >= len(digits):
                res.append(curr_comm)
                return
            for key in keypad[digits[index]]:
                helper(index + 1, curr_comm + key)
            
        helper(0, "")
        return res
            
            
        