"""IG: few.pz"""
def main():
    """ Main function """
    _, vote, most_vote, most_free, list_score = int(input()), int(input()), '', 0, []
    for _ in range(vote):
        each_vote = int(input())
        list_score.append(each_vote)
        if list_score.count(each_vote) > most_free:
            most_free = list_score.count(each_vote)
            most_vote = each_vote
    if most_free > (vote/2):
        print(most_vote, most_free)
    else:
        print('0', most_free)
main()
