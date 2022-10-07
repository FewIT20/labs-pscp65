"""IG: few.pz"""
def main():
    """Main function"""
    score = []
    data = []
    mean = 0
    value = 0
    countable = int(input())
    for _ in range(countable):
        txt = input()
        data.append(txt)
        txt = txt.split("\t")
        score.append(float(txt.pop(1)))
    mean = (sum(score))/countable
    student_of_mean_score = sorted(score)
    student_of_mean_score.reverse()
    for i in student_of_mean_score:
        if i <= mean:
            value = score.index(i)
            print(data[value])
            break
main()
