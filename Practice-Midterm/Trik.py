"""IG: few.pz"""
def calculate_ball(current, text):
    """Calculation of ball"""
    if text == "A":
        if current == 1:
            current = 2
        elif current == 2:
            current = 1
    elif text == "B":
        if current == 2:
            current = 3
        elif current == 3:
            current = 2
    elif text == "C":
        if current == 1:
            current = 3
        elif current == 3:
            current = 1
    return current

def main():
    """Main function"""
    current = 1
    text = input()
    for character in text:
        current = calculate_ball(current, character)
    print(current)
main()
