#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101', base=10))

# 把1作为参数的一部分
min1 = functools.partial(min, 1)
print(min1(5, 7, 2))

# 把10作为参数的一部分
max2 = functools.partial(max, 10)
print(max2(5, 7, 2))
