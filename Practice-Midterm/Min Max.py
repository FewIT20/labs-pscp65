"""IG: few.pz"""
def main():
    """Main function"""
    round = int(input())
    min_value = 0
    max_value = 0
    for i in range(round):
        value = int(input())
        if i == 0:
            #Initialize min_value and max_value
            min_value = value
            max_value = value
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    print("%d" % (min_value))
    print("%d" % (max_value))
        
main()
