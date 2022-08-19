"""IG: fewpz"""
 
 
def main():
    """Main functions"""
    time = int(input())
 
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
 
    print(day, hour, minutes, seconds)
 
 
main()