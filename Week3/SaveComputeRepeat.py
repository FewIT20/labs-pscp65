"""IG: fewpz"""
 
 
def main():
    """Main functions"""
    start_here = 492137954293754252786
    millseconds = start_here
    seconds = millseconds // 1000
    millseconds = millseconds % 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
 
    print("%d %d %d %d %d" % (days, hours, minutes, seconds, millseconds))
 
main()