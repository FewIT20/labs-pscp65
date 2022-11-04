"""IG: few.pz"""
import json

def main():
    """ Main function """
    attack = sorted(json.loads(input()), reverse=True)
    deffend = sorted(json.loads(input()), reverse=True)
    defpin, att_pin, limit, value = 0, 0, len(deffend), 0
    while defpin != limit:
        if attack[att_pin] > deffend[defpin]:
            value += attack[att_pin]
            att_pin += 1
        defpin += 1
    print(value)
main()
