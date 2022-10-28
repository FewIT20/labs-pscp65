"""IG: few.pz"""
def main():
    """ Main function """
    gho = {"EMF Level 5" : ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade']\
            , "Ghost Writing" : ['Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei']\
            , "Fingerprints" : ['Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith']\
            , "Spirit Box" : ['Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith']\
            , "Freezing Temperatures" : ['Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei']\
            , "Ghost Orb" : ['Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei']\
            , "No evidence" : ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade', 'Demon', \
            'Mare', 'Poltergeist', 'Spirit', 'Wraith', 'Yurei']}
    value = list(set(gho[input()]).intersection(gho[input()]).intersection(gho[input()]))
    value.sort()
    if len(value) == 0:
        print("Not yet discovered")
    else:
        print(*value, sep="\n")
main()
