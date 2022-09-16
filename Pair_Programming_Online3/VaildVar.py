"""IG: few.pz"""
def true_or_false(x_val):
    """True or False"""
    if x_val == "True" or x_val == "False":
        return True
    return False

def checker_one(x_val):
    """Check one"""
    if x_val == "None" or x_val == "and" or x_val == "as" or x_val == "assert":
        return True
    if x_val == "async" or x_val == "await" or x_val == "break" or x_val == "class":
        return True
    return False


def checker_two(x_val):
    """Check one"""
    if x_val == "continue" or x_val == "def" or x_val == "del" or x_val == "elif":
        return True
    if x_val == "else" or x_val == "except" or x_val == "finally" or x_val == "for":
        return True
    return False

def checker_three(x_val):
    """Check one"""
    if x_val == "from" or x_val == "global" or x_val == "if" or x_val == "import":
        return True
    if x_val == "in" or x_val == "is" or x_val == "lambda" or x_val == "nonlocal":
        return True
    return False


def checker_four(x_val):
    """Check one"""
    if x_val == "not" or x_val == "or" or x_val == "pass" or x_val == "raise":
        return True
    if x_val == "return" or x_val == "try" or x_val == "while" or x_val == "with":
        return True
    if x_val == "yield":
        return True
    return False

def checker_valuable(var):
    """Checker valuable"""
    if true_or_false(var) or checker_one(var) or checker_two(var) or checker_three(var) \
        or checker_four(var):
        return True
    return False

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
            if y_val in pattern or checker_valuable(valuable) or valuable[0].isdigit() \
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
