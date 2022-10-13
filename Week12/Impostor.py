"""IG: few.pz"""
import json

def main():
    """Main function"""
    player, dead, alive, impostor = {}, {}, {}, 0
    while True:
        txt = input()
        if txt.lower() == "start":
            continue
        if txt.lower() == "end":
            break
        if txt[0] == "{":
            player.update(json.loads(txt))
        else:
            dead.update({txt:player[txt]})
    for i in player:
        if i not in dead:
            alive.update({i:player[i]})
    for i in alive:
        if player[i] == "Impostor":
            impostor += 1
    print(str(impostor)+" Impostor Remains", "***Alive***", sep="\n")
    for i in sorted(alive.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
    print("***Dead***")
    for i in sorted(dead.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
main()
