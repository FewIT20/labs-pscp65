"""IG: few.pz"""
def main():
    """Main function"""
    a_val = int(input())
    b_val = int(input())
    c_val = int(input())
    d_val = int(input())
    cap = d_val // a_val
    milk = cap
    if b_val == 0:
        print(milk)
    else:
        while True:
            more = (cap // b_val) * c_val
            milk += more
            cap = 0
            cap += (cap % b_val)
            cap += more
            more = 0
            if cap < b_val:
                break
        print(milk)
main()
