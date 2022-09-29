"""IG: few.pz"""
def calculate_grade(total_score):
    """Calculate grade"""
    if total_score >= 80:
        return "A"
    elif total_score >= 75:
        return "B+"
    elif total_score >= 70:
        return "B"
    elif total_score >= 65:
        return "C+"
    elif total_score >= 60:
        return "C"
    elif total_score >= 55:
        return "D+"
    elif total_score >= 50:
        return "D"
    return "F"

def main():
    """Main function"""
    score = int(input())
    midterm_score = int(input())
    final_score = int(input())
    
    grade = calculate_grade(score + midterm_score + final_score)
    print(grade)
main()
