from bigfloat import *
from random import getrandbits
from LazyCartesianProduct import LazyCartesianProduct

bits = 3
size = 24
sets = [(range(bits)) for x in range(size ** 2)]
total = BigFloat.exact(bits ** (size ** 2))
p = total.precision
context = precision(p)
cp = LazyCartesianProduct(sets, context)

# - get last index
# index = sub(total, BigFloat.exact(1), context=context)
# - get arbitrary index
# index = sub(total, BigFloat.exact('2e99', precision=p), context=context)

# get random index
index = mul(total, BigFloat.exact(
    '0.' + str(getrandbits(p)), precision=p), context=context)

print(f"Precision: {p}\nIndex: {index}\nValue: {cp.entryAt(index)}")
