"""IG: few.pz"""
def main():
    """Main function"""
    menu = []
    while True:
        course = input()
        if course == "DONE":
            break
        elif course == "CLOSED":
            return print("Full Course: [] Reversed: []")
        elif course == "SOMETHING'S WRONG":
            menu.clear()
            continue
        elif course[0:10:] == "Can't do: ":
            menu.remove(course[10::])
        else:
            text = course.split(" #")
            if text[1].isnumeric():
                menu.insert(int(text[1])-1, text[0])
            else:
                menu.append(text[0])
    print("Full Course: " + str(menu), end=" ")
    menu.reverse()
    print("Reversed: " + str(menu))
main()
