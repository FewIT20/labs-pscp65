"""Resistor"""
def band11(band_1):
    """check band_1"""
    if band_1 == 'Black':
        return 0
    elif band_1 == 'Brown':
        return 1
    elif band_1 == 'Red':
        return 2
    elif band_1 == 'Orange':
        return 3
    elif band_1 == 'Yellow':
        return 4
    else:
        return band12(band_1)

def band12(band_1):
    """check band_1"""
    if band_1 == 'Green':
        return 5
    elif band_1 == 'Blue':
        return 6
    elif band_1 == 'Purple':
        return 7
    elif band_1 == 'Grey':
        return 8
    elif band_1 == 'White':
        return 9
    else:
        return 'Error'

def band21(band_2):
    """check band_2"""
    if band_2 == 'Black':
        return 0
    elif band_2 == 'Brown':
        return 1
    elif band_2 == 'Red':
        return 2
    elif band_2 == 'Orange':
        return 3
    elif band_2 == 'Yellow':
        return 4
    else:
        return band22(band_2)

def band22(band_2):
    """check band_2"""
    if band_2 == 'Green':
        return 5
    elif band_2 == 'Blue':
        return 6
    elif band_2 == 'Purple':
        return 7
    elif band_2 == 'Grey':
        return 8
    elif band_2 == 'White':
        return 9
    else:
        return 'Error'

def band31(mult):
    """check band_3"""
    if mult == 'Black':
        return 1
    elif mult == 'Brown':
        return 10
    elif mult == 'Red':
        return 100
    elif mult == 'Orange':
        return 1000
    elif mult == 'Yellow':
        return 10000
    else:
        return band32(mult)

def band32(mult):
    """check band_3"""
    if mult == 'Green':
        return 100000
    elif mult == 'Blue':
        return 1000000
    elif mult == 'Purple':
        return 10000000
    elif mult == 'Gold':
        return 0.1
    elif mult == 'Silver':
        return 0.01
    else:
        return 'Error'

def band41(tolerance):
    """check band_4"""
    if tolerance == 'Brown':
        return 1
    elif tolerance == 'Red':
        return 2
    elif tolerance == 'Green':
        return 0.5
    elif tolerance == 'Blue':
        return 0.25
    else:
        return band42(tolerance)

def band42(tolerance):
    """check band_4"""
    if tolerance == 'Purple':
        return 0.1
    elif tolerance == 'Grey':
        return 0.05
    elif tolerance == 'Gold':
        return 5
    elif tolerance == 'Silver':
        return 10
    else:
        return 'Error'

def main():
    """Resistor"""
    band_1 = input()
    band_2 = input()
    mult = input()
    tolerance = input()
    num_1 = band11(band_1)
    num_2 = band21(band_2)
    num_3 = band31(mult)
    num_4 = band41(tolerance)
    if num_1 == 'Error' or num_2 == 'Error' or num_3 == 'Error'\
        or num_4 == 'Error':
        print('Error')
    else:
        number = int(str(num_1)+str(num_2))
        print('%.4f'%((number*num_3)-((number*num_3)*(num_4/100))))
        print('%.4f'%((number*num_3)+((number*num_3)*(num_4/100))))
main()
