"""IG: few.pz"""
def main():
    """Main function"""
    value = input().split()
    for i in range(len(value)):
        value[i] = int(value[i])
    value.remove(max(value))
    print(max(value) * min(value))
main()
