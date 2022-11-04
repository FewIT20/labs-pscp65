"""IG: few.pz"""
def main():
    """ Main function """
    books = []
    while True:
        price = input()
        if price == "ENTER":
            break
        books.append(int(price))
    books.sort()
    if len(books) < 20:
        bonus = min(2, len(books) // 6)
    else:
        bonus = len(books) // 5
    print(sum(books[bonus:]))
main()
