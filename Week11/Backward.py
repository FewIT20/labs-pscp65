"""IG: few.pz"""
def main():
    """Main function"""
    value = []
    while True:
        x_val = input()
        if x_val == "NULL":
            break
        value.append(x_val)
    value.reverse()
    print(*value, sep="\n")
main()
