"""IG: few.pz"""
def recessive_loop(x_val):
    """Recessive loop"""
    value = 0
    for i in x_val:
        value += int(i)
    if len(str(value)) != 1:
        value = recessive_loop(str(value))
    return value

def main():
    """Main function"""
    while True:
        x_val = input()
        value = 0
        if x_val == "0":
            break
        else:
            value = recessive_loop(x_val)
            print(value)
main()
