import time
from random import randint


class UnionFind:

    def __init__(self):
        self.set = None

    def find(self, x):
        rewrite = {x}
        i = x
        while self.set[i] != i:
            rewrite.add(i)
            i = self.set[i]

        if len(rewrite) > 1:
            for ind in rewrite:
                self.set[ind] = i

        return i

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a != b:
            if x < y:
                self.set[y] = a
            else:
                self.set[x] = b


class Task:

    def __init__(self, deadline=None, penalty=None):
        self.deadline = deadline
        self.penalty = penalty

    def __repr__(self):
        return f"{self.deadline}: {self.penalty}"

    def __str__(self):
        return self.__repr__()


def frm_str(s):
    s = s.split(",")
    ans = []
    for st in s:
        st = list(map(int, st.replace("[", "").replace("]", "").split(":")))
        ans.append(Task(st[0], st[1]))
    return ans


test1 = [Task(3, 25), Task(4, 10), Task(1, 30), Task(3, 50), Task(3, 20)]
test2 = [Task(3, i) for i in range(20)]
test3 = "[7: 24, 6: 125, 3: 56, 2: 117, 3: 44, 5: 41, 3: 31, 7: 37, 5: 106, 5: 49, 8: 114, 5: 117, 5: 123, 4: 68," \
        " 6: 76]"

test3 = frm_str(test3)


def dec_dls(tasks: list):
    for task in tasks:
        task.deadline -= 1
    pass


def inc_dls(tasks: list):
    for task in tasks:
        task.deadline += 1
    pass


def timer(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.20f} seconds")
        # return the result of the decorated function execution
        return result

    # return reference to the wrapper function
    return wrapper


@timer
def solution_with_uf(tasks):
    dec_dls(tasks)
    tasks.sort(key=lambda tsk: tsk.penalty, reverse=True)
    uf = UnionFind()
    uf.set = list(range(len(tasks)))
    ans = [None for _ in range(len(tasks))]
    pen = 0
    for task in tasks:
        ind = task.deadline
        if ans[ind] is None:
            ans[ind] = task
        else:
            ind = uf.find(ind)
            if ind > 0:
                ind -= 1
                ans[ind] = task
            else:
                pen += task.penalty
                ind = len(tasks) - 1
                if ans[ind] is None:
                    ans[ind] = task
                else:
                    ind = uf.find(ind)
                    ind -= 1
                    ans[ind] = task
        if ind >= 1 and ans[ind - 1] is not None:
            uf.union(ind - 1, ind)
        if ind < len(tasks) - 1 and ans[ind] is not None:
            uf.union(ind, ind + 1)

    inc_dls(tasks)
    return ans, pen


@timer
def solution(tasks):
    dec_dls(tasks)
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
    inc_dls(tasks)
    return ans, pen


tests = [test1, test2] + [[Task(randint(1, 8), randint(20, 150)) for i in range(j)]
                          for j in range(1000, 2000, 50)]

number = 0
for test in tests:
    print(number, sep=" ")
    # print(test)
    a = test.copy()
    res1 = solution_with_uf(test)
    res2 = solution(a)
    # print(res1, res2, sep="\n")
    assert res1 == res2
    number += 1

# print(solution_with_uf(test3))
# print(solution(test3))
