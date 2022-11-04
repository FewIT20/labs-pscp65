"""IG: few.pz"""
def child(dad, mom, bloods):
    """ Find child bloodtype """
    if ("+" in dad+mom) == False:
        _ = [bloods.remove(i) for i in ["A+", "B+", "AB+", "O+"] if i in bloods]
    if ("A" in dad+mom) == False:
        _ = [bloods.remove(i) for i in ["A+", "A-", "AB+", "AB-"] if i in bloods]
    if ("B" in dad+mom) == False:
        _ = [bloods.remove(i) for i in ["B+", "B-", "AB+", "AB-"] if i in bloods]
    if ("AB" in dad+mom) == True:
        _ = [bloods.remove(i) for i in ["O+", "O-"] if i in bloods]
    if ("O" in dad+mom) == True:
        _ = [bloods.remove(i) for i in ["AB+", "AB-"] if i in bloods]
    return bloods

def find_parent(parent, kid, bloods):
    """ Find missing parent """
    chances = [i for i in bloods if kid in child(parent, i, [i for i in bloods])]
    return "IMPOSSIBLE" if len(chances) == 0 else "{" + (" ".join(chances)) + "}"

def main():
    """ Main function """
    dad, mom, kid = input().split()
    bloods = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    if kid == "?":
        print(dad, mom, "{" + (" ".join(child(dad, mom, [i for i in bloods]))) + "}")
    if mom == "?":
        print(dad, find_parent(dad, kid, [i for i in bloods]), kid)
    if dad == "?":
        print(find_parent(mom, kid, [i for i in bloods]), mom, kid)
main()
