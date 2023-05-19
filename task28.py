from random import randint
import math


class Bitset:

    def __init__(self, value=0, length=0):
        self.value = value
        self.length = length or math.ceil(math.log2(value))

    def __repr__(self):
        return f"Bitset({bin(self.value)[2:][::-1]})"

    def __str__(self):
        return bin(self.value)[2:][::-1]

    def __getitem__(self, ind):
        return (2 ** ind & self.value) >> ind

    def __setitem__(self, key, val):
        assert val == 0 or val == 1
        self.value = (self.value | (val << key))

    def __len__(self):
        return self.length

    def __iter__(self):
        for k in range(self.length):
            yield self[k]


class IP:

    def from_string(self, s):
        s = s.split(".")
        self.first = int(s[0])
        self.second = int(s[1])
        self.third = int(s[2])
        self.fourth = int(s[3])

    def __init__(self, s=None):
        if s is None:
            self.first = 0
            self.second = 0
            self.third = 0
            self.fourth = 0
        else:
            self.from_string(s)

    def __str__(self):
        return f"{self.first}.{self.second}.{self.third}.{self.fourth}"

    def __repr__(self):
        return self.__str__()


class BF:

    def __init__(self, dim, funcs=None):
        self.bitset = Bitset(length=dim)
        if funcs is not None:
            self.funcs = funcs
        else:
            self.funcs = []

    def insert(self, val):
        for func in self.funcs:
            self.bitset[func(val)] = 1

    def lookup(self, val):
        for func in self.funcs:
            if self.bitset[func(val)] == 0:
                return False
        return True


def get_rand_hash_func(dim):
    a1 = randint(1, dim - 1)
    a2 = randint(1, dim - 1)
    a3 = randint(1, dim - 1)
    a4 = randint(1, dim - 1)

    def hash_func(ip):
        return (a1 * ip.first + a2 * ip.second + a3 * ip.third + a4 * ip.fourth) % dim

    return hash_func


def get_size_and_quantity(max_quant_el, probability):
    assert probability <= 1

    b = math.ceil(math.log(probability) / (math.log(2) * math.log(1 / 2)))

    return b * max_quant_el, math.ceil(math.log(2) * b)


DIM = 20
PROBABILITY = 0.001

ip_arr1 = [IP(s) for s in "28.84.68.8, 252.248.87.43, 167.129.44.17," 
                          " 248.32.239.250, 22.92.101.97, 123.235.24.124, 143.188.167.22, 109.46.102.113".split(",")]
# ip_arr2 = []
#

#
# for i in range(DIM):
#     new_item = IP(f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}")
#     ip_arr2.append(new_item)
#
# print(ip_arr2)

size, quant = get_size_and_quantity(DIM, PROBABILITY)

hash_funcs = []
for i in range(quant):
    hash_funcs.append(get_rand_hash_func(size))


fil = BF(dim=size, funcs=hash_funcs)

for el in ip_arr1:
    fil.insert(el)


for el in ip_arr1:
    print(fil.lookup(el))

for i in range(10000):
    if fil.lookup(IP("1.1.1.1")):
        print("OMG")
