"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    value = value.replace("[", "")
    value = value.replace("]", "")
    value = value.split(",")
    for text in value:
        print(text[-1])
main()
