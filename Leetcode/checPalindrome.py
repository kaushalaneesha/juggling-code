class Solution:
	# @param A : integer
	# @return an integer
    def isPalindrome(self, A):
        num = A
        if A < 0: # negative numbers are not palindrome
            return 0
        # get the number of digits
        count = 0
        while A:
            A = A // 10 
            count += 1
        n = count // 2
        
        while n > 0:
            num1 = num // (10 ** (count-1))
            num2 = num % 10
            if num1 != num2:
                return 0
            # Update number num (remove 1st and last digit)
            num = num % (10 ** (count - 1))
            num = num // 10
            n -= 1
            count -= 2
        return 1

s = Solution()
print(s.isPalindrome(12121))