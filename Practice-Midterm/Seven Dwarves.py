"""IG: few.pz"""

def main():
    """ Main function """
    crewmate = [int(input()) for _ in range(9)]
    for imposter_a in crewmate:
        remaining_crewmate = [*crewmate]
        remaining_crewmate.remove(imposter_a)
        for imposter_b in remaining_crewmate:
            party = [*remaining_crewmate]
            party.remove(imposter_b)
            if sum(party) == 100:
                for i in party:
                    print(i)
                return
    print("ERROR")

main()