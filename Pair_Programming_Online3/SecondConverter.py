"""IG: few.pz"""
def main():
    """Main function"""
    custom_time = int(input())
    seconds_in_seconds = int(input())
    mins_in_seconds = int(input())
    hours_in_seconds = int(input())

    mins = custom_time // seconds_in_seconds
    seconds = custom_time % seconds_in_seconds
    hours = mins // mins_in_seconds
    mins = mins % mins_in_seconds
    hours = hours % hours_in_seconds
    print("%d:%d:%d" % (hours, mins, seconds))
main()
