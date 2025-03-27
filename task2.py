from utils.tree import Tree

def connect_four_ab(contents, turn, max_depth):
    tree = Tree(contents, turn, max_depth)
    tree.generate_state_space()
    e = tree.minimax_ab(tree.root, tree.root.turn)
    return f"{e.get_col()}\n{tree.nodes_examined}"

if __name__ == '__main__':
    result = connect_four_ab("yyyrrry,rryyyry,yrryryr,yyyrrry,rryyy..,....r..", "red", 6)