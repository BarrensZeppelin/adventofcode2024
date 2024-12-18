#!/usr/bin/env pypy3
# 332/311
from __future__ import annotations

from util import *

replace_stdin()

res = 0

a, b = [], []
for l in lines():
    x, y = ints(l)
    a.append(x)
    b.append(y)

# C1 = Counter(a)
C2 = Counter(b)

# for x, y in zip(sorted(a), sorted(b)):
#     res += abs(y - x)

for x in a:
    res += x * C2[x]


# print(res)
submit(res)
