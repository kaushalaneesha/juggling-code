"""
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""

def rotateCharacter(c, rotation_factor, initial_char):
  return chr((ord(c) - ord(initial_char) + rotation_factor) % 26 + ord(initial_char))

def rotateNumber(c, rotation_factor):
  return str((int(c) + rotation_factor ) % 10)
  
def rotationalCipher(input_str, rotation_factor):
  # rotation_factor should just be remainder with 26 for alphabets and 10 for numbers. 
  # if character is a number we will use this formula = (char + rotating_factor_num) - 10. Assuming rotating factor is already udpated by 1. 
  # if character alphabet = (char + rotating_factor_alpha) - 26.
  rotation_factor_num =  rotation_factor % 10
  rotation_factor_alpha =  rotation_factor % 26
  res = []
  for char in input_str:
    if char.isdigit():
      new_char = rotateNumber(char, rotation_factor_num)
    elif ord(char) in range(65,91):
      new_char = rotateCharacter(char, rotation_factor_alpha, 'A')
    elif ord(char) in range(97,123):
      new_char = rotateCharacter(char, rotation_factor_alpha, 'a')
    else:
      new_char = char
    res.append(new_char)
  return "".join(res)


print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))

