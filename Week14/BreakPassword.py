"""IG: few.pz"""
import hashlib

def main():
    """ Main function """
    encrypted = input()
    for number in range(0, 100000):
        value = str("%05d" % (number))
        hashing = hashlib.sha512(value.encode())
        if str(hashing.hexdigest()).upper() == encrypted:
            print("%05d" % (number))
main()
