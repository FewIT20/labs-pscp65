"""IG: few.pz"""
def calculate_kaprekar(number):
    """Calculate kaprekar"""
    x_val = []
    for i in number:
        x_val.append(int(i))
    value = []
    calculate = ""
    while x_val:
        sk_upper = x_val[0]
        for i in x_val:
            if i < sk_upper:
                sk_upper = i
        value.append(sk_upper)
        x_val.remove(sk_upper)
    for i in value:
        calculate += str(i)
    return calculate

def main():
    """Main function"""
    value = input()
    count = 1
    while value != "6174":
        if value == "6174":
            print(count)
            break
        if len(str(value)) < 4:
            value = value + "0"
        else:
            sk_number_value = calculate_kaprekar(value)[::-1]
            number = int(sk_number_value) - int(sk_number_value[::-1])
            if number == 6174:
                print(count)
                break
            else:
                value = str(number)
                count = count + 1

main()
