"""IG: few.pz"""
import string

def caesar_cipher(raw, shift):
    """Caesar Cipher"""
    result = ""
    for i in raw:
        if i in string.ascii_letters:
            if i.isupper():
                c_index = ord(i) - ord("A")
                new_index = (c_index + shift) % 26
                new_unicode = new_index + ord("A")
                new_char = chr(new_unicode)
                result = result + new_char
            else:
                if i != " ":
                    c_index = ord(i) - ord("a")
                    new_index = (c_index + shift) % 26
                    new_unicode = new_index + ord("a")
                    new_char = chr(new_unicode)
                    result = result + new_char
                else:
                    result += i
        else:
            result += i
    return result

def main():
    """Main function"""
    key = int(input())
    word = input()
    result = caesar_cipher(word, key)
    print(result)
main()
