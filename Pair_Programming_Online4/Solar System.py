"""IG: few.pz"""
def main():
    """Main function"""
    text = input()
    planet = []
    word = ''
    for i in text:
        if i == ' ':
            planet.insert(0, word)
            word = ''
        else:
            word += i
    planet.insert(0, word)
    planet = planet[::-1]
    idx1, idx2, idx3 = planet[0], planet[-1], planet.index("Sun")
    if idx1 == "Sun":
        print("Hot: "+ planet[1])
        print("Cool: "+ idx2)
    elif idx2 == "Sun":
        print("Hot: "+ planet[-2])
        print("Cool: "+ idx1)
    else:
        print("Hot: %s %s"%(planet[idx3-1], planet[idx3+1]))
        if abs(planet.index(idx1)-idx3) == abs(planet.index(idx2)-idx3):
            print("Cool: %s %s"%(idx1, idx2))
        elif abs(planet.index(idx1)-idx3) > abs(planet.index(idx2)-idx3):
            print("Cool: %s"%idx1)
        elif abs(planet.index(idx1)-idx3) < abs(planet.index(idx2)-idx3):
            print("Cool: %s"%idx2)
main()
