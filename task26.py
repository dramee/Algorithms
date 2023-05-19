

class FreqStack:
    # create dict to monitor frequency
    def __init__(self):
        self.stack = []
        self._freq_dict = {}

    def push(self, val):
        self.stack.append(val)
        if val not in self._freq_dict.keys():
            self._freq_dict[val] = 1
        else:
            self._freq_dict[val] += 1

    def pop(self):
        if self.stack:
            elements_to_pop = [self.stack[0]]
            freq = self._freq_dict[elements_to_pop[0]]
            for key, val in self._freq_dict.items():
                if val > freq:
                    elements_to_pop = []
                    freq = val
                    elements_to_pop.append(key)
                elif val == freq:
                    elements_to_pop.append(key)

            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i] in elements_to_pop:
                    return self.stack.pop(i)

