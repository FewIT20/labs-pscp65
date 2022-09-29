"""IG: few.pz"""
def main():
    """Main function"""
    value = input()
    if value.islower():
        print("All Small Letter")
    elif value.isupper():
        print("All Capital Letter")
    else:
        print("Mix")
main()
