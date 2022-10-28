"""IG : few.pz"""
def score_total(pin, score):
    """return total score"""
    if "/" == score:
        return 10 if "X" in pin else 0 if "-" == pin[0] else int(pin[0])
    elif "X" == score:
        return last_frame(pin)

def last_frame(pin):
    """return score last frame"""
    score, score1 = 0, 0
    for i in pin:
        if i == "X":
            score += 10
        elif i == "/":
            score += 10
            score1 = 0
        else:
            score1 += int(i) if i != "-" else 0
    return score + score1

def main():
    """Bowling-Reddit"""
    bord = input().split()
    bord1 = bord[:-1]+list(bord[-1])
    score_bord = [0]
    for i in range(9):
        pin = bord[i]
        score = score_bord[-1]
        if "X" in pin:
            if "X" not in bord1[i+1]:
                score += 10 + score_total(bord[i+1], "X")
            else:
                count = 0
                score += 10
                for j in bord1[i+1:]:
                    if "X" in j:
                        score += 10
                        count += 1
                    else:
                        score += score_total(j, "/")
                        break
                    if count == 2:
                        break
        elif "/" in pin:
            score += 10 + score_total(bord[i+1][0], "/")
        else:
            score += score_total(pin, "X")
        score_bord.append(score)
    score_bord.append(last_frame(bord[-1])+score_bord[-1])
    print(score_bord[-1])

main()
