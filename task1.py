from utils.tree import Tree

def connect_four_mm(contents, turn, max_depth):
    tree = Tree(contents, turn, max_depth)
    tree.generate_state_space()
    tree.display_tree(tree.root)

    e = tree.minimax(tree.root, 0, max_depth, tree.root.turn)
    return f"{e.get_col()}\n{tree.nodes_examined}"

if __name__ == '__main__':
    result = connect_four_mm("yrrr.yy,yrr......,.......,.......,.......,.......", "red", 1)
    print(result)
