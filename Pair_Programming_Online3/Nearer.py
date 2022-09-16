"""IG: few.pz"""
def main():
    """Main function"""
    distance_alice = int(input())
    distance_bob = int(input())
    distance_icecream = int(input())
    distance_alice_to_icecream = abs(distance_icecream - distance_alice) # abs() is absolute value
    distance_bob_to_icecream = abs(distance_icecream - distance_bob)
    if distance_alice_to_icecream < distance_bob_to_icecream:
        print("Alice %d" % distance_alice_to_icecream)
    elif distance_alice_to_icecream > distance_bob_to_icecream:
        print("Bob %d" % distance_bob_to_icecream)
    else:
        print("Sundaes %d" % distance_alice_to_icecream)
main()
