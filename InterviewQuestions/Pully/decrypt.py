import base64
import re
import requests
import msgpack

def to_list(stringList):
  stringList = stringList.split('[')[1]# removes "["
  stringList = stringList.split(']')[0]# removes "]"
  stringList = stringList.split(',') # gets objects in the list
  return [int(text) for text in stringList] 
    
def convert_ascii(s: str):
    """
    String to be converted from ascii
    """
    lst = to_list(s)
    return "".join(chr(num) for num in lst)

def remove_non_hex(s: str):
    """
    Removes non-hex characters from the string
    """
    return ''.join(c for c in s if c in '0123456789abcdef')

def rotate_right(s: str, rotation_factor):
    """
    Rotate the string circularly to the right by rotation_factor positions.
    """
    return s[-rotation_factor:] + s[:-rotation_factor]


def xor_decrypt(hex_str, key):
    """
    Decrypt hex encoded string using XOR with a given key.
    """
    try:
        decoded_bytes = bytes.fromhex(hex_str)
        key_bytes = key.encode()
        decrypted_bytes = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(decoded_bytes))
        return decrypted_bytes.hex()
    except Exception as e:
        print(f"Error decrypting: {e}")
        return None

def unscramble(scrambled: str, original_pos_base64: str):
    unscrambled = [''] * len(scrambled)
    original_positions = msgpack.unpackb(base64.b64decode(original_pos_base64))
    for i, pos in enumerate(original_positions):
        unscrambled[pos] = scrambled[i]
    return "".join(unscrambled)

def decypt(input):
    """
    Json containing the encrypted_path and encryption_method
    """
    encryption_method = input.get('encryption_method')
    encrypted_path = input.get('encrypted_path')[5:]
    decypted_path = "task_"
    # print(encrypted_path)
    # print(encryption_method)
    # print()
    if encryption_method == "nothing":
        return decypted_path + encrypted_path
    elif encryption_method == "converted to a JSON array of ASCII values":
        return decypted_path + convert_ascii(encrypted_path)
    elif encryption_method == "inserted some non-hex characters":
        return  decypted_path + remove_non_hex(encrypted_path)
    elif encryption_method.find("circularly rotated left by ") != -1:
        m = re.match(r'circularly rotated left by (.*)', encryption_method)
        rotation_factor = int(m.group(1))
        return  decypted_path + rotate_right(encrypted_path, rotation_factor)
    elif encryption_method.startswith("hex decoded, encrypted with XOR, hex encoded again"):
        key = encryption_method.split(": ")[1]
        return  decypted_path + xor_decrypt(encrypted_path, key)
    elif encryption_method.startswith("scrambled! original positions as base64 encoded"):
        original_pos_base64 = encryption_method.split(": ")[1]
        return  decypted_path + unscramble(encrypted_path, original_pos_base64)

base = "https://ciphersprint.pulley.com/"
path = "aneeshakaushal1992@gmail.com"
for i in range(7):
    response = requests.get(base + path)
    input = response.json()
    print("--------------------------")
    print(input)
    path = decypt(input)
    print(path)
