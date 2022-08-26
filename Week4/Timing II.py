"""IG: few.pz"""
 
 
def main():
    """Main function"""
    time = int(input())
    seconds = time % 60
    minutes = time//60
    hours = minutes//60
    minutes = minutes % 60
    days = hours//24
    hours = hours % 24
    if days <= 9999:
        print("%0.4d:%.2d:%.2d:%.2d" % (days, hours, minutes, seconds))
    elif days > 9999:
        print("ERR_:__:__:__")
 
 
main()
