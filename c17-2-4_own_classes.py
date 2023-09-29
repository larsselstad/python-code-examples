import numpy as np
import operator

class Paper(object):
    def __init__(self, name, start, last):
        self.name = name
        self.start = start
        self.last = last

    def getLast(self):
        return self.last


class Stock(Paper):
    def __init__(self, name, start, last):
        super().__init__(name, start, last)


stocks = np.array([
    Stock('eqnr', 34.2, 34.8),
    Stock('akrbp', 31.2, 32.0),
    Stock('var', 23.1, 22.7)])

print(stocks)

for istock in stocks:
    print(istock.name, istock.getLast())

sorted_stocks = sorted(stocks, key=operator.attrgetter('name'))

for istock in stocks:
    print(istock.name, istock.getLast())

for istock in sorted_stocks:
    print(istock.name, istock.getLast())

# get sum of last
values = [istock.getLast() for istock in stocks ]
print(values)
print(np.sum(values))