"""IG: few.pz"""
def main():
    """Main function"""
    arr = []
    for _ in range(10):
        arr.append(int(input()) % 42)
    print(len(set(arr)))
        
main()
