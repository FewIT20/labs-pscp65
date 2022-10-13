"""IG: few.pz"""
def main():
    """Main function"""
    student = []
    while True:
        value = input()
        if value == "END":
            break
        student.append(value[:4])
    old_year = 0
    for i in sorted(set(student)):
        year = i[:2]
        print(year if year != old_year else "--", int(i[2:4]), student.count(i))
        old_year = year
main()
