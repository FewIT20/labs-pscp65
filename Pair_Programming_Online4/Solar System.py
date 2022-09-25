"""IG: few.pz"""
def find_index_planet_sun(x_val, index):
    """Find index of planet in sun"""
    for i in range(x_val.count(" ")):
        value = x_val[0:x_val.find(" ")]
        if index == i:
            return value
        x_val = x_val[x_val.find(" ")+1:]
        
def calculate_finding_a_planet_hot_and_cool(x_val, count_of_x_val, index):
    """Calculate finding a planet hot and cool"""
    planet_hot = ''
    planet_cool = ''
    planet_hot = str(find_index_planet_sun(x_val, index - 1))
    if count_of_x_val >= 3:
        planet_cool = str(find_index_planet_sun(x_val, 0))
    elif count_of_x_val == 2:
        planet_cool = str(find_index_planet_sun(x_val, index - 1))
    return planet_hot, planet_cool

def main():
    """Main function"""
    value =  str(input())
    index = -1
    planet_hot = ""
    planet_cool = ""
    
    x_val = value
    count_of_value = value.count(" ")
    for i in range(count_of_value):
        y_val = x_val[0:x_val.find(" ")]
        if y_val.lower() == "sun":
            index = i
        x_val = x_val[x_val.find(" ")+1:]
    if index == -1:
        #If the sun is not in the list of planets
        pass
    
    elif index == 0:
        planet_hot = str(find_index_planet_sun(value, index + 1))
        if count_of_value >= 3:
            planet_cool = str(find_index_planet_sun(value, count_of_value - 1))
        elif count_of_value == 2:
            planet_cool = str(find_index_planet_sun(value, index + 1))
    elif index == count_of_value or index == count_of_value - 1:
        planet_hot, planet_cool = calculate_finding_a_planet_hot_and_cool(value, count_of_value, index)
    else:
        if count_of_value > 3:
            planet_hot = str(find_index_planet_sun(value, index - 1)) + " " + str(find_index_planet_sun(value, index + 1))
            if count_of_value >= 5 and int(count_of_value / 2) == index:
                planet_cool = str(find_index_planet_sun(value, 0)) + " " + str(find_index_planet_sun(value, count_of_value - 1))
            else:
                if index == 1 or int(count_of_value / 2) > index:
                    planet_cool = str(find_index_planet_sun(value, count_of_value - 1))
                elif index == count_of_value - 2 or int(count_of_value / 2) < index:
                    planet_cool = str(find_index_planet_sun(value, 0))
        else:
            planet_hot = str(find_index_planet_sun(value, index - 1)) + " " + str(find_index_planet_sun(value, index + 1))
            planet_cool = str(find_index_planet_sun(value, index - 1)) + " " + str(find_index_planet_sun(value, index + 1))
                
    #Solution of the problem
    print('Hot: ' + planet_hot)
    print('Cool: ' + planet_cool)
main()