from utils.tree import Tree

def connect_four_ab(contents, turn, max_depth):
    tree = Tree(contents, turn, max_depth)
    tree.generate_state_space()
    e = tree.minimax_ab(tree.root, tree.root.turn)
    # alr a win state/no moves left
    if e is None:
        return f"0\n1"
    return f"{e.get_col()}\n{tree.nodes_examined}"

if __name__ == '__main__':
    result = connect_four_ab("yyyrrry,rryyyry,yrryryr,yyyrrry,rryyy..,....r..", "red", 6)
    # result = connect_four_ab("rrrrrry,yyyyyyr,rrrrrry,yyyyyyr,rrrrrry,yyyyyy.", "red", 2)
    # result = connect_four_ab("rrr....,.......,.......,.......,.......,.......", "red", 0)
    print(result)