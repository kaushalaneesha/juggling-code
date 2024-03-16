class Solution:
   def intToRoman(self, num: int):
    roman = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
        }
    romanized = ''

    for base, symb in roman.items():
        print((num // base))
        romanized += symb * (num // base)
        num %= base
    else:
        return romanized

s = Solution()
print(s.intToRoman(58))