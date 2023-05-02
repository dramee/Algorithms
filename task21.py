class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    ans = []
    stc = [root]
    while len(stc) > 0:
        tmp = []
        for a in stc:
            if a is None:
                ans.append("N")
            else:
                ans.append(str(a.val))
            if a is not None:
                tmp.append(a.left)
                tmp.append(a.right)
        stc = tmp
    ans = ", ".join(ans)
    return ans


def deserialize(data):
    data = data.split(", ")
    if data[0] == "N":
        return None
    root = TreeNode(data[0])
    stc = [root]
    i = 1
    while len(stc) > 0:
        if data[i] != "N":
            stc[0].left = TreeNode(int(data[i]))
            stc.append(stc[0].left)
        i += 1
        if data[i] != "N":
            stc[0].right = TreeNode(int(data[i]))
            stc.append(stc[0].right)
        i += 1
        stc.pop(0)
    return root


class Codec:
    pass


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)
tree.right.left.left = TreeNode(6)
tree.right.left.right = TreeNode(7)

ser = Codec()

print(serialize(tree))
new_tree = deserialize(serialize(tree))
print(serialize(new_tree))
