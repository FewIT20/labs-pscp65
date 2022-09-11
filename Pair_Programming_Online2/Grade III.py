"""IG: few.pz"""
def convert_to_grader(score):
    """Convert to grader"""
    value = 0
    if score >= 95 and score <= 100:
        value = 4
    elif score >= 90 and score < 95:
        value = 3.5
    elif score >= 85 and score < 90:
        value = 3
    elif score >= 80 and score < 85:
        value = 2.5
    elif score >= 75 and score < 80:
        value = 2
    elif score >= 70 and score < 75:
        value = 1.5
    elif score >= 65 and score < 70:
        value = 1
    elif score >= 60 and score < 65:
        value = 0.5
    elif score > 0 and score < 60:
        value = 0
    return value

def main():
    """Main function"""
    count = int(input())
    score_total = 0
    for _ in range(count):
        score_total += convert_to_grader(float(input()))
    print("%.2f" % ((int((score_total/count)*100))/100))
main()
