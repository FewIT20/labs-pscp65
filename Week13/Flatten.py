"""IG: few.pz"""
import json

def main(value: list):
    """ Main function """
    black_pink = []
    for raw in value:
        if isinstance(raw, list):
            black_pink += main(raw)
        else:
            black_pink.append(raw)
    black_pink.sort(reverse=True)
    return black_pink

print(main(json.loads(input())))
