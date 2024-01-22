import time
from random import randint


class UnionFind:

    def __init__(self, amount):
        self.set = [i for i in range(amount)]
        self.ranks = [0 for i in range(amount)]
        self.bounds = self.set

    def find(self, x):
        # save indexes to rewrite
        rewrite = {x}
        i = x
        # find the root
        while self.set[i] != i:
            rewrite.add(i)
            i = self.set[i]
        # rewriting
        if len(rewrite) > 1:
            for ind in rewrite:
                self.set[ind] = i

        return i

    def union(self, x, y):
        # find roots
        a = self.find(x)
        b = self.find(y)
        if a != b:
            # connect right part to left
            self.bounds[a] = self.bounds[b] = min(self.bounds[a], self.bounds[b])

            if self.ranks[a] > self.ranks[b]:
                self.set[b] = a
            else:  # member_2.rank <= member_1.rank
                self.set[a] = b
                if self.ranks[a] == self.ranks[b]:
                    self.ranks[b] += 1


class Task:

    def __init__(self, deadline=None, penalty=None):
        self.deadline = deadline
        self.penalty = penalty

    def __repr__(self):
        return f"{self.deadline}: {self.penalty}"

    def __str__(self):
        return self.__repr__()


# reading data from string
def frm_str(s):
    s = s.split(",")
    ans = []
    for st in s:
        st = list(map(int, st.replace("[", "").replace("]", "").split(":")))
        ans.append(Task(st[0], st[1]))
    return ans


# funcs for check default test
# def dec_dls(tasks: list):
#     for task in tasks:
#         task.deadline -= 1
#     pass
#
#
# # def inc_dls(tasks: list):
# #     for task in tasks:
# #         task.deadline += 1
# #     pass


test1 = [Task(2, 25), Task(3, 10), Task(0, 30),
         Task(2, 50), Task(2, 20)]
test2 = [Task(3, i) for i in range(100)]
test3 = "[7: 24, 6: 125, 3: 56, 2: 117, 3: 44, 5: 41, 3: 31, 7: 37, 5: 106, 5: 49, 8: 114, 5: 117, 5: 123, 4: 68," \
        " 6: 76]"

test3 = frm_str(test3)


def solution_with_uf(tasks):
    tasks.sort(key=lambda tsk: tsk.penalty, reverse=True)
    uf = UnionFind(len(tasks))
    uf.set = list(range(len(tasks)))
    ans = [None for _ in range(len(tasks))]
    pen = 0
    for task in tasks:
        ind = task.deadline
        # check in deadline
        if ans[ind] is None:
            ans[ind] = task
        else:
            # if not try to find days before
            ind = uf.find(ind)
            # if > 0 - we can write task to this day
            if ind > 0:
                ind -= 1  # it needs for opportunity to use "union" in general situations
                ans[ind] = task
            # else we have penalty and will make task at the end
            else:
                pen += task.penalty
                # go to the last day
                ind = len(tasks) - 1
                if ans[ind] is None:
                    ans[ind] = task
                else:
                    # same as above
                    ind = uf.find(ind)
                    ind -= 1
                    ans[ind] = task
        # check neighbours for union for element
        if ind >= 1 and ans[ind - 1] is not None:
            uf.union(ind - 1, ind)
        if ind < len(tasks) - 1 and ans[ind] is not None:
            uf.union(ind, ind + 1)

    return ans, pen


print(solution_with_uf(test1))


# @timer
def solution(tasks):
    # nothing interesting
    tasks.sort(key=lambda tsk: tsk.penalty, reverse=True)
    ans = [None for _ in range(len(tasks))]
    pen = 0
    for task in tasks:
        ind = task.deadline
        if ans[ind] is None:
            ans[ind] = task
        else:
            while ind > 0 and ans[ind] is not None:
                ind -= 1
            if ans[ind] is None:
                ans[ind] = task
            else:
                pen += task.penalty
                ind = len(tasks) - 1
                while ans[ind] is not None:
                    ind -= 1
                ans[ind] = task
    return ans, pen


def incorrect(tasks):
    tasks.sort(key=lambda x: x.penalty, reverse=True)
    pen = 0
    for i in range(len(tasks)):
        if tasks[i].deadline > i + 1:
            pen += tasks[i].penalty
    return pen


tests = [test1, test2] + [[Task(randint(1, 8), randint(20, 150)) for i in range(j)]
                          for j in range(1000, 5000, 50)]

number = 0
for test in tests:
    # print(number, end=": ")
    # print(test)
    test_c = test.copy()
    res1 = solution_with_uf(test)
    res2 = incorrect(test_c)
    # print(res1, res2, sep="\n")
    # if res1 != res2:
    #     # print("False")
    # else:
    #     print("True")
    number += 1

# print(solution_with_uf(test3))
# print(solution(test3))
