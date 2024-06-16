# 1. find the average length of word in sentence
import collections
from typing import List


sentence = "My name is Aneesha"

def average_word_length(sentence: str) -> float:
    sum_length = 0
    word_count = 0
    if not sentence:
        return 0
    words = sentence.split(" ")
    for word in words:
        if word: # Ingore multiple spaces
            word_count += 1
            sum_length = len(word)
    
    return sum_length / word_count


print(average_word_length(sentence))

# 2. Validate the ipv4 address
# IP addresses are expressed as a set of four numbers — an example address might be 192.158.1.38. Each number in the set can range from 0 to 255.
ip_address = "127.0.0.b"
def validate_ip(ip_address):
    ip_groups = ip_address.split(".")
    if len(ip_groups) != 4:
        return False
    for group in ip_groups:
        try:
            if not 0 < int(group) < 255:
                return False
        except:
            return False
    return True
        
print(validate_ip(ip_address))

# 3. for a list array=[['D'],['A','B'],['A','C'],['C','A']] find the number of followers
def find_followers(input: List[List[chr]]) -> dict:
    followers = collections.defaultdict(int)
    for elem in input:
        if len(elem) > 1:
            followers[elem[0]] += 1
        elif elem[0] not in followers:
            followers[elem[0]] = 0
    return followers
    
print(find_followers([['D'],['A','B'],['A','C'],['C','A']]))

# Find the maximum number that can be constructed from a string of digits.
num = "9129012198"
def largest_integer(num: str) -> int:
    lst_num = list(num)
    lst_num.sort(reverse=True)
    return int("".join(lst_num))

print(largest_integer(num))


