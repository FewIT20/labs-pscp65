"""IG: few.pz"""

import hashlib

def main():
    """ Main function """
    password = input().encode('utf-8')
    hashed_password = hashlib.sha512(password).hexdigest().upper()
    print(hashed_password)
main()
