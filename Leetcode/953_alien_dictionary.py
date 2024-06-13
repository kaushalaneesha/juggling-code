from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_lst = {char: i for i, char in enumerate(order)}
        for j in range(0, len(words) - 1):
            for i in range(20):
                if len(words[j]) <= i:
                    break
                elif len(words[j+1]) <= i:
                    return False
                elif order_lst.get(words[j][i]) > order_lst.get(words[j+1][i]):
                    return False
                elif order_lst.get(words[j][i]) != order_lst.get(words[j+1][i]):
                    break
        return True
    
s = Solution()
print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))



