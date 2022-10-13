"""IG: few.pz"""
def sort_by_value(var):
    """Sort by value"""
    char = var[0]
    return ord(char) + (100 if char.isupper() else 0)

def main(string):
    """Main function"""
    for char, count in sorted({i: string.count(i) for i in string}.items(), key=sort_by_value):
        print(char, ":", "".join(["-" if i % 5 else "-|" for i in range(1, count+1)]).rstrip("|"))
main(input())
