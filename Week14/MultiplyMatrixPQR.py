"""IG: few.pz"""
def addlistbyfewza(num1, num2, fewza007):
    """fewza007"""
    for _ in range(num1):
        lstf = []
        for _ in range(num2):
            few = int(input())
            lstf.append(few)
        fewza007.append(lstf)
    return fewza007

def main():
    """ Main function """
    num1, num2, num3 = int(input()), int(input()), int(input())
    alst = addlistbyfewza(num1, num2, [])
    blst = addlistbyfewza(num2, num3, [])
    for i in alst:
        for j in range(len(blst[0])):
            sumbyfew, countfew = 0, 0
            for k in i:
                sumbyfew += k * int(blst[countfew][j])
                countfew += 1
            print(sumbyfew, end=" ")
        print()
main()
