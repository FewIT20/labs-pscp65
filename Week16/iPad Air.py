"""IG: few.pz"""


def main():
    """ Main function """
    color_lst = ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue']
    disk_lst = ['64 GB', '256 GB']
    connection_lst = ['Wi-Fi', 'Wi-Fi + Cellular']

    color = input()
    disk = input()
    connection = input()

    disk += ' GB'

    if color not in color_lst or disk not in disk_lst or connection not in connection_lst:
        print('Not Available')
    else:
        if disk == "64 GB":
            if connection == "Wi-Fi":
                print(19900)
            else:
                print(24400)
        elif disk == "256 GB":
            if connection == "Wi-Fi":
                print(24900)
            else:
                print(29400)


main()
