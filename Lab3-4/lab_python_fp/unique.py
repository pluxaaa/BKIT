from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.data = list(items)
        #print(self.data)
        self.index = 0

        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index += 1
                if self.ignore_case == True and type(current) == str:
                    current = current.lower()
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


# data1 = ['a', 'a', 'b', 'B']
# print("Uniq: ", list(Unique(data1)))
#
# data2 = gen_random(10, 1, 3)
# print("Uniq: ", list(Unique(data2)))
