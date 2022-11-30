"""Thank you ขอบคุณที่เราได้พบเจอกัน"""
def main():
    """Love you, I say, good bye my dearest!"""
    value = int(input())
    lst = []
    if value < 0:
        lst = [int(i) for i in range(0, value - 1, -1)]
    else:
        lst = [int(i) for i in range(0, value + 1)]
    print(lst)
main()
