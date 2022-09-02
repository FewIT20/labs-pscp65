"""IG: few.pz"""
def main():
    """Main function"""
    starter = int(input())
    breaker = int(input())
    stepper = int(input())
    for i in range(starter, breaker, stepper):
        print("%d" % i)
main()
