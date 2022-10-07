"""IG: few.pz"""
def main():
    """Main function"""
    amount = int(input())
    count = int(input())
    passenger_of_list_string = [] #list var is string
    passenger_of_list_integer = [] #list var is integer
    at_home = 0
    for _ in range(count):
        bus = input().split()
        passenger_of_list_string.append(bus)
    passenger_of_list_string.sort(key=lambda i: int(i[0]))
    for i in passenger_of_list_string:
        stage_bus_stop = int(i[0])
        if len(passenger_of_list_integer) != 0:
            passenger_of_list_integer2 = passenger_of_list_integer.copy()
            for arrive in passenger_of_list_integer:
                if arrive == stage_bus_stop:
                    passenger_of_list_integer2.remove(arrive)
                    at_home += 1
            passenger_of_list_integer = passenger_of_list_integer2
        for j in range(1, len(i)):
            if len(passenger_of_list_integer) == amount:
                break
            if stage_bus_stop < int(i[j]):
                passenger_of_list_integer.append(int(i[j]))
    print(at_home)
main()
