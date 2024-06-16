class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] # Bracket and its position
        for i, ch in enumerate(s):
            if ch == ')' and stack and stack[-1][0] == '(':
                stack.pop()
            elif ch == '(' or ch == ')': 
                stack.append((ch, i))

        positions_to_remove = set()
        for _, pos in stack:
            positions_to_remove.add(pos)
        
        res = []
        for i in range(len(s)):
            if i not in positions_to_remove:
                res.append(s[i])
        return "".join(res)