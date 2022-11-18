"""IG: few.pz"""


def main():
    """ Main function """
    check_item = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
                  "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    check_taste = ["Sweet", "Sour", "Salty"]
    item_list = []
    taste_list = []
    not_in_check = []
    while True:
        item = input()
        if item == "Cook":
            break
        if item not in item_list:
            item_list.append(item)
        if item not in check_item:
            not_in_check.append(item)
    while True:
        taste = input()
        if taste == "End":
            break
        if taste not in taste_list:
            taste_list.append(taste)
    if not_in_check != []:
        print("This is not Pad Thai!!!")
    elif item_list != check_item:
        print("This is bad!")
    elif item_list == check_item:
        if taste_list == check_taste:
            print("Delicious!")
        else:
            print("Not Bad...")


main()
