"""IG: few.pz"""
def median(value):
    """Midpoint of a list"""
    length_of_list = len(value)
    x_value = sorted(value)
    return (x_value[length_of_list//2-1]/2.0+x_value[length_of_list//2]/2.0,\
        x_value[length_of_list//2])[length_of_list % 2] if length_of_list else None

def main():
    """Main function"""
    countable = int(input())
    numbers = []
    for _ in range(countable):
        numbers.append(int(input()))
    print("%.1f" % median(numbers))
main()
