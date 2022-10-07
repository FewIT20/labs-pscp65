"""IG: few.pz"""
def main():
    """Main function"""
    countable = []
    specific_of_cat = []
    while True:
        text = input().split(", ")
        if text == ["IT\'S A DOG"]:
            countable.pop()
            continue
        if text == ['END']:
            break
        countable += text
    for i in range(len(countable)):
        if countable[i] not in specific_of_cat:
            specific_of_cat.append(countable[i])
    specific_of_cat.sort()
    for i in range(len(specific_of_cat)):
        print("%s %d %d"%(specific_of_cat[i], (countable.index(specific_of_cat[i])+1),\
            countable.count(specific_of_cat[i])))
main()
