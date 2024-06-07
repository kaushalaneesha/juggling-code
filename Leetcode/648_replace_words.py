"""
    Approach: 
    1. Create a trie from dictionary of all the roots. 
    2. Iterate over the words formed by spliting the sentence by space. 
    3. For each word. Find the shortest root or in other words shortest prefix. Logic:
        3.1. Iterate over its characters. 
                3.1.1 Stop when you can find those prefix of characters, i.e. word[:i+1] in the trie of 
                roots. 
                3.1.2 If no match is found in the trie or you reach end of the word, return word. 
    4. Combine all the shortest root found by space and return as a string
    Complexity: 
    Time: O(d.w + s.w) 
    Space: O(n)

    d -> number of words in the dictionary
    w -> length of words
    s -> number of words in a sentence
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.is_end = False # to mark the end of the node
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            child = current.children.setdefault(char, TrieNode())
            current = child
        current.is_end = True

    def shortest_root(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                return word
            if current.children[char].is_end:
                return word[:i+1]
            # else continue to the next character to see if its a match
            current = current.children[char]
        return word
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Create trie from dictionary
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        # Split the sentence and pass to the shortest_root function. Using python map for the same
        return " ".join(map(trie.shortest_root, sentence.split(" ")))


# Test case
s = Solution()
replaced_word = s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
expected = "the cat was rat by the bat"
if expected == replaced_word:
    print("Test passed")
else:
    print("Test failed")
