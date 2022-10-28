"""IG: few.pz"""
import math

def main(rabbit, stairs, carrot):
    """Rabbit"""
    few1, few2, few3 = 0, 0, 0
    if rabbit > carrot:
        few1, few2, few3 = int(rabbit-carrot), math.floor(stairs-((carrot/2)*(carrot+1))), 0
        if few1 <= -1 or few2 <= -1 or few3 <= -1:
            sud = math.floor((((2*stairs)+(1/4))**(1/2))-(1/2))
            few1, few2, few3 = int(
                rabbit-sud), math.floor(stairs-((sud/2)*(sud+1))), int(carrot-sud)
    elif ((rabbit/2)*(rabbit+1)) <= stairs:
        few1, few2, few3 = 0, math.floor(
            stairs-((rabbit/2)*(rabbit+1))), carrot-rabbit
    elif ((rabbit/2)*(rabbit+1)) > stairs:
        sud = math.floor((((2*stairs)+(1/4))**(1/2))-(1/2))
        few1, few2, few3 = int(
            rabbit-sud), math.floor(stairs-((sud/2)*(sud+1))), int(carrot-sud)
    if few1 == 0 and few2 == 0 and few3 == 0:
        print('Ahhahaha')
    else:
        print(few1, few2, few3)

main(int(input()), int(input()), int(input()))
