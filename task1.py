from utils.tree import Tree

def connect_four_mm(contents, turn, max_depth):
    tree = Tree(contents, turn, max_depth)
    tree.generate_state_space_tree()
    # tree.display_tree(tree.root)

    e = tree.minimax(tree.root, 0, max_depth, tree.root.turn)
    print(e.get_col())
    print(tree.nodes_examined)

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm("ryryyy.,rryyry.,rryryr.,..y....,.......,.......", "red", 4)
