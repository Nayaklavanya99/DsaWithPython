class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
print(node0)
node0.left=node1
node0.right=node2

print(node0.left.key)


tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance(data,tuple) and len(data)==3:
        node = TreeNode(data[1])
        node.left=parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)
print(tree2.left.right)
print(tree2.right.right.left.key)


def traverse_in_order(node):
        if node is None:
            return []
        return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))
tree3 = traverse_in_order(tree2)
print(tree3)