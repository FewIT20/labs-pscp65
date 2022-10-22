"""IG: few.pz"""
def check(result, words):
    """ Check word is in sentence """
    for word in words:
        if word in result:
            return True
    return False

def main():
    """ Main function """
    encoded = input()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()

    words = ['The', 'the', 'What', 'what', 'Where', 'where', 'When', 'when']
    result = ""
    while 1:
        for char in encoded:
            if char.isupper():
                result += upper[(upper.index(char) + 1) % 26]
            elif char.islower():
                result += lower[(lower.index(char) + 1) % 26]
            else:
                result += char
        encoded = result
        if check(result, words):
            break
        result = ""
    print(encoded)
main()
