from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        """
         Start from the last source so that we do not implact the order of 
         original string's index
         If source matches at index. Replace it
         Else skip it 
        """
        sl = list(s)
        # TODO: sort all three together and start from back
        for i, source, target in sorted(list(zip(indices, sources, targets)), reverse = True):
            if s[i:i+len(source)] == source:
                # If there is a match
                # replace the substring
                sl = sl[:i] + list(target) + sl[i+len(source):]
                # print(sl)
            else:
                continue
        return "".join(sl)
        