from utils.tree import Tree

def connect_four_mm(contents, turn, max_depth):
    tree = Tree(contents, turn, max_depth)
    tree.generate_state_space_tree()
    tree.display_tree(tree.root)
    return ''

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 3)
