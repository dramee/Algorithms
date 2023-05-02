class BST:

    def __init__ (self, val=0, left=None, right=None, balance=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance = balance


# functions for check
def serialize(root):
    ans = []
    stc = [root]
    while len(stc) > 0:
        tstc = []
        for a in stc:
            if a is None:
                ans.append("N")
            else:
                ans.append(str(a.val))
            if a is not None:
                tstc.append(a.left)
                tstc.append(a.right)
        stc = tstc
    ans = ",".join(ans)
    return ans


def deserialize(data):
    data = data.split(",")
    if data[0] == "N":
        return None
    root = BST(data[0])
    stc = [root]
    i = 1
    while len(stc) > 0:
        if data[i] != "N":
            stc[0].left = BST(int(data[i]))
            stc.append(stc[0].left)
        i += 1
        if data[i] != "N":
            stc[0].right = BST(int(data[i]))
            stc.append(stc[0].right)
        i += 1
        stc.pop(0)
    return root


def small_left_rotate(bst):
    # check that bst is not None and have right child
    if not bst or not bst.right:
        return
    # save root and child of node, which will become root and delete it from right tree
    left_c = bst.right.left
    bst.right.left = None
    # save new root and add left child to old_root
    new_root = bst.right
    bst.right = left_c
    new_root.left = bst
    bst = new_root
    return bst


def small_right_rotate(bst):
    # check that bst is not None and have right child
    if not bst or not bst.left:
        return
    # save root and child of node, which will become root and delete it from right tree
    right_c = bst.left.right
    bst.left.right = None
    # save new root and add left child to old_root
    new_root = bst.left
    bst.left = right_c
    new_root.right = bst
    bst = new_root
    return bst


def big_left_rotate(bst):
    bst.right = small_right_rotate(bst.right)
    bst = small_left_rotate(bst)
    return bst


def big_right_rotate(bst):
    bst.left = small_left_rotate(bst.left)
    bst = small_right_rotate(bst)
    return bst


def get_depth(bst):

    if bst is None:
        return 0

    return max(get_depth(bst.left), get_depth(bst.right)) + 1


def balance_bst(bst):

    if bst is None:
        return 0, None

    right_h, bst.right = balance_bst(bst.right)
    left_h, bst.left = balance_bst(bst.left)
    bst.balance = right_h - left_h
    h = max(right_h, left_h) + 1

    if right_h - left_h > 1:

        if bst.right.balance >= 0:
            bst = small_left_rotate(bst)
            bst.balance = -1 + bst.right.balance
            return h - bst.right.balance, bst

        if bst.right.balance == -1:
            bst = big_left_rotate(bst)
            bst.balance = 0
            return h - 1, bst
        else:
            bst = big_left_rotate(bst)
            bst.left = balance_bst(bst.left)[1]
            bst = balance_bst(bst)[1]
            right_h = get_depth(bst.right)
            left_h = get_depth(bst.left)
            bst.balance = right_h - left_h
            return max(right_h, left_h) + 1, bst

    elif right_h - left_h < -1:

        if bst.left.balance <= 0:
            bst = small_right_rotate(bst)
            bst.balance = 1 + bst.left.balance
            return h + bst.left.balance, bst

        if bst.left.balance == 1:
            bst = big_right_rotate(bst)
            bst.balance = 0
            return h - 1, bst
        else:
            bst = big_right_rotate(bst)
            bst.right = balance_bst(bst.right)[1]
            bst = balance_bst(bst)[1]
            right_h = get_depth(bst.right)
            left_h = get_depth(bst.left)
            bst.balance = right_h - left_h
            return max(right_h, left_h) + 1, bst

    return h, bst


s = "1, null, 15, 14, 17, 7, null, null, null, 2, 12, null, 3, 9, null, null, null, null, 11, N, N"
s = s.replace("null", "N").replace(", ", ",")
print(s)
tree = deserialize(s)
tree = balance_bst(tree)[1]
print(get_depth(tree))
print(serialize(tree))
