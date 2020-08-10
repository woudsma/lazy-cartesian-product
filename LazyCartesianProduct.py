import math
from bigfloat import *


class LazyCartesianProduct:
    def __init__(self, sets, context):
        self.sets = sets
        self.context = context
        self.divs = []
        self.mods = []
        self.maxSize = BigFloat.exact(1)
        self.precompute()

    def precompute(self):
        for i in self.sets:
            self.maxSize = mul(self.maxSize, BigFloat.exact(
                len(i)), context=self.context)
        factor = BigFloat.exact(1)
        for i in range((len(self.sets) - 1), -1, -1):
            items = BigFloat.exact(
                str(len(self.sets[i])), precision=self.context.precision)
            self.divs.insert(0, factor)
            self.mods.insert(0, items)
            factor = mul(factor, items, context=self.context)

    def entryAt(self, n):
        if less(n, BigFloat.exact(0)) or greaterequal(n, self.maxSize):
            raise IndexError
        combination = []
        for i in range(0, len(self.sets)):
            d = div(n, self.divs[i], context=self.context)
            m = mod(floor(d, context=self.context),
                    self.mods[i], context=self.context)
            combination.append(int(m))
        return combination
