"""Thank you ขอบคุณที่เราได้พบเจอกัน"""
def main():
    """Love you, I say, good bye my dearest!"""
    ranks = [int(i) for i in input().split(",")]
    ranked = sorted(ranks, reverse=True)
    value = [str(ranked.index(i) + 1) for i in ranks]
    string_builder = ","
    string_builder = string_builder.join(value)
    print(string_builder)
main()
