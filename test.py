"""Bowling-Reddit"""

def main(bord):
    """Bowling-Reddit"""
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
    print(*score_bord[1:])

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

def bowling():
    """input score"""
    pin = input().split()
    score_lst = []
    frame = ""
    for score in pin:
        if len(frame) == 0 and score == "10":
            score_lst.append("X")
            print("X", end=" ")
        elif frame == "-" and score == "10":
            frame += "/"
        elif len(frame) == 1 and frame != "-":
            if int(frame) + int(score) == 10:
                frame += "/"
            else:
                frame += score
        else:
            frame += "-" if score == "0" else score
        if len(frame) == 2:
            score_lst.append(frame)
            print(*list(frame), end=" ")
            frame = ""
    print()
    score_lst[9] = score_lst[9]+score_lst[10] if len(score_lst) == 11 else score_lst[9]
    print(score_lst[:10])
    main(score_lst[:10])


bowling()