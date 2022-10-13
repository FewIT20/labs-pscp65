"""IG: few.pz"""
import json

def main():
    """Main function"""
    value = input()
    json_paser = ['0']
    test = float(input())
    value = json.loads(value)
    for key in value:
        if value[key] >= test:
            json_paser.append('%s %.2f' %(key, float(value[key])))
        else:
            pass
    if len(json_paser) >= 2:
        json_paser.remove('0')
    json_paser.sort()
    for i in json_paser:
        if i == "0":
            print("Nope")
            break
        else:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))
main()
