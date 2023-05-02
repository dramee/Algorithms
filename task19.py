# from random import randint


class ListNode:

    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

    def add_node(self, val):
        new_nd = ListNode(val=val)
        self.nxt = new_nd

    def __str__(self):
        t = self
        s = ""
        while t is not None:
            s += f"{t.val} "
            t = t.nxt
        s = s.strip()
        s = s.replace(" ", "->")
        return s

    def del_node(self):
        self.nxt = None

    def peek_tail(self):
        t1 = self
        while t1.nxt:
            t1 = t1.nxt
        return t1

    def add_tail(self, val):
        t2 = self.peek_tail()
        t2.add_node(val)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __le__(self, other):
        return self.val < other.val or self.val == other.val


class MinHeap:

    def _sift_down(self, ind):
        mc = self.get_min_child(ind)
        if mc is not None:
            while mc is not None and self.data[ind] > self.data[mc]:
                self.data[ind], self.data[mc] = self.data[mc], self.data[ind]
                ind = mc
                mc = self.get_min_child(ind)

    def make_heap(self):
        st = (self.size - 1) // 2
        for j in range(st, -1, -1):
            self._sift_down(j)

    def get_min_child(self, ind):
        if 2 * ind + 1 < self.size:
            if ind * 2 + 2 >= self.size:
                return ind * 2 + 1
            else:
                if self.data[2 * ind + 1] <= self.data[2 * ind + 2]:
                    return 2 * ind + 1
                else:
                    return 2 * ind + 2
        else:
            return None

    def get_parent(self, ind):
        if self.size > 0 and ind > 0:
            return (ind - 1) // 2
        else:
            return None

    def _sift_up(self, ind):
        p = self.get_parent(ind)
        if p is not None:
            while p is not None and self.data[ind] < self.data[p]:
                self.data[ind], self.data[p] = self.data[p], self.data[ind]
                ind = p
                p = self.get_parent(ind)

    def insert(self, val):
        self.size += 1
        self.data.append(val)
        self._sift_up(self.size - 1)

    def extract_min(self):
        if self.size > 0:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            d = self.data.pop()
            self.size -= 1
            self._sift_down(0)
            return d

    def peek_min(self):
        return self.data[0]

    def __init__(self, data=None):
        if data is None:
            self.data = []
            self.size = 0
        else:
            self.data = data
            self.size = len(data)
            self.make_heap()

    def __str__(self):
        return self.data.__str__()

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.size > 0:
            for k in range(self.size):
                yield self.data[k]
        else:
            yield []


test_list1 = ListNode(val=1)
start = test_list1
for i in range(2, 7):
    new_node = ListNode(val=i)
    start.nxt = new_node
    start = start.nxt

test_list2 = ListNode(val=7)
start = test_list2
for i in range(10, 15):
    new_node = ListNode(val=i)
    start.nxt = new_node
    start = start.nxt

test_list3 = ListNode(val=9)
start = test_list3
for i in range(10, 11):
    new_node = ListNode(val=i)
    start.nxt = new_node
    start = start.nxt

print(test_list1, test_list2, test_list3, sep="\n")

lists = [test_list1, test_list2, test_list3]

heap = MinHeap([node for node in lists])

new_list = ListNode()
head = new_list
first = False
while heap.data:
    tmp = heap.extract_min()
    if not first:
        head.val = tmp.val
        first = True
    else:
        head.nxt = tmp
        head = head.nxt
    if tmp.nxt is not None:
        heap.insert(tmp.nxt)

print(new_list)
