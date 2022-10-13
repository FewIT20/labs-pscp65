"""IG: few.pz"""
def main():
    """Main function"""
    countries = dict()
    for _ in range(int(input())):
        value = input().split(" ")
        countries[value[0]] = tuple(map(int, value[1:]))
    sorted_countries = sorted(countries.items(), key=lambda a: sum(a[1]), reverse=True)
    sorted_countries.sort(key=lambda a: a[0])
    sorted_countries.sort(key=lambda a: a[1], reverse=True)
    rank = 0
    keep = 0
    old = 0
    for country, score in sorted_countries:
        score_sum = sum(score)
        score = " ".join(map(str, score))
        if score != old:
            rank += keep
            keep = 0
            rank += 1
        elif rank != 0:
            keep += 1
        print(rank, country, score, score_sum)
        old = score
main()
