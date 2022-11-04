"""IG: few.pz"""
import json
def run_node(node_map, node_parent, node_can_links):
    """elegant"""
    while node_parent:
        node_child = [i for i in node_map[node_parent.pop()] if i not in node_can_links]
        node_can_links += node_child
        node_parent += node_child
    return node_can_links

def main():
    """ Main function """
    node_map = json.loads(input().replace("'", '"'))
    node_first = input()
    node_can_links = run_node(node_map, [node_first], [node_first])
    print(sorted(set(node_can_links)))
main()
