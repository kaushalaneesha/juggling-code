def minimumNumberOfDeletions(S):
    def helper(start, end, op):
        # base condition
        if start >= end:
            return op
        while start < end and S[start] == S[end]:
            start += 1
            end -= 1
        if start >= end:
            return op
        else:
            return min(helper(start+1, end, op+1), helper(start, end-1, op+1))
    
    return helper(0, len(S)-1, 0)

print(minimumNumberOfDeletions("aebcbda"))