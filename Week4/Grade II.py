"""IG: few.pz"""
def convert_text(value):
    """Covert text to grade"""
    text = "ERR"
    if value >= 95 and value <= 100:
        text = "A"
    elif value >= 90 and value < 95:
        text = "B+"
    elif value >= 85 and value < 90:
        text = "B"
    elif value >= 80 and value < 85:
        text = "C+"
    elif value >= 75 and value < 80:
        text = "C"
    elif value >= 70 and value < 75:
        text = "D+"
    elif value >= 65 and value < 70:
        text = "D"
    elif value >= 60 and value < 65:
        text = "F+"
    elif value > 0 and value < 60:
        text = "F"
    elif value < 0 or value > 100:
        text = "ERR"

    return text

def main():
    """Main function"""
    score = float(input())
    print(convert_text(score))
main()
