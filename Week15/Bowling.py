"""IG: few.pz"""


def main():
    """ Calculate """
    inp = input().split()

    scores = []
    behavior = []

    frames = []
    while len(inp) != 0:
        score1 = int(inp.pop(0))

        if score1 == 10:
            scores.append(score1)
            behavior.append('Strike')

            frames.append('X')
            continue

        if len(inp) == 0:
            scores.append(score1)
            break
        score2 = int(inp.pop(0))

        if score1 + score2 == 10:
            scores.append(score1)
            scores.append(score2)
            behavior.append('Spare')

            frames.append(str(score1) if score1 != 0 else '-')
            frames.append('/')
        else:
            scores.append(score1)
            scores.append(score2)
            behavior.append('Normal')

            frames.append(str(score1) if score1 != 0 else '-')
            frames.append(str(score2) if score2 != 0 else '-')

    total_scores = []
    for i in range(len(behavior)):
        if i == 10:
            break
        if behavior[i] == 'Normal':
            prev_score = 0
            if len(total_scores) != 0:
                prev_score = total_scores[-1]
            total_scores.append(prev_score + scores.pop(0) + scores.pop(0))
        elif behavior[i] == 'Spare':
            prev_score = 0
            if len(total_scores) != 0:
                prev_score = total_scores[-1]
            score1 = scores.pop(0)
            score2 = scores.pop(0)
            score3 = 0
            if i == 9:
                score3 = scores.pop(0)
            extra_score = 0
            if len(scores) != 0:
                extra_score = scores[0]
            total_scores.append(prev_score + score1 +
                                score2 + score3 + extra_score)
        elif behavior[i] == 'Strike':
            prev_score = 0
            if len(total_scores) != 0:
                prev_score = total_scores[-1]
            score = scores.pop(0)
            extra_score1 = 0
            extra_score2 = 0
            if len(scores) >= 1:
                extra_score1 = scores[0]
            if len(scores) >= 2:
                extra_score2 = scores[1]
            total_scores.append(prev_score + score +
                                extra_score1 + extra_score2)

    total_scores = list(map(str, total_scores))
    print(' '.join(frames))
    print(' '.join(total_scores))


main()
