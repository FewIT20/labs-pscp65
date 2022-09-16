"""IG: few.pz"""
import keyword

def main():
    """Main function"""
    count = int(input())
    pattern = '''!()-[];:'",<>./?\\@#$%^+=&*~'''
    checker = ""
    for _ in range(count):
        valuable = input()
        if valuable[-1] == " ":
            #Check last index string
            valuable = valuable[:-1]
        for y_val in valuable:
            if y_val in pattern or keyword.iskeyword(valuable) or valuable[0].isdigit() \
                or " " in valuable[1:]:
                print("Invalid")
                checker = ""
                break
            else:
                checker = checker + y_val
            if valuable == checker:
                print("Valid")
                checker = ""
                break
        
main()
