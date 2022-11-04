"""IG: few.pz"""
def check(sym, num, state):
    """ Check function """
    if state == 'YES':
        if sym == '<':
            return [i for i in range(int(num))]
        elif sym == '>':
            return [i for i in range(int(num)+1, 101)]
        elif sym == '=':
            return [int(num)]
    elif state == 'NO':
        if sym == '<':
            return [i for i in range(int(num), 101)]
        elif sym == '>':
            return [i for i in range(int(num)+1)]
        elif sym == '=':
            return [i for i in range(101) if int(num) != i]

def main():
    """ Main function """
    ans = []
    while True:
        txt = input()
        if txt == 'END':
            break
        lst = txt.split()
        ans.append(check(lst[0], lst[1], lst[2]))
    if len(ans) > 0:
        set_a = set(ans[0])
        for i in range(1, len(ans)):
            set_a = set_a.intersection(set(ans[i]))
        print(*sorted(set_a))
    else:
        print(*range(101))
main()
