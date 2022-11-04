"""ISBN"""
def main():
    """ISBN"""
    id_card_text = input()
    id_card = [int(i) if i != "X" else 10 for i in id_card_text if i != "-"]
    sum_id_card = -sum(([i*j for i, j in zip(id_card[:-1], range(10, 1, -1))]))%11
    if sum_id_card == 10:
        sum_id_card = "X"
    if id_card_text[-1] == str(sum_id_card):
        print("Yes")
    else:
        print("No", sum_id_card)

main()
