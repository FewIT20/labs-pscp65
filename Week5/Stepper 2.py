"""IG: few.pz"""
def main():
    """Main function"""
    starter = int(input())
    breaker = int(input())
    if breaker < starter:
        for i in range(starter, breaker-1, -1):
            print(i)
    elif breaker >= starter:
        for i in range(starter, breaker+1, 1):
            print(i)
main()
