"""IG: few.pz"""
import json

def main():
    """ Main function """
    dic1 = {}
    dic2 = {}
    txt1 = json.loads(input())
    txt2 = json.loads(input())
    for i in txt1:
        dic1[i] = dic1.get(i, 0)+1
    for i in txt2:
        dic2[i] = dic2.get(i, 0)+1
    num = int(input())
    ans = 0
    for i in sorted(dic1):
        if i > num:
            break
        if num-i in dic2:
            ans += (dic1[i] * dic2[num-i])
    print(ans)
main()
