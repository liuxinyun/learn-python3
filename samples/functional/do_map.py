#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def normalize(name):
    r1 = name.upper()[0]
    r2 = name.lower()[1:]
    return r1 + r2

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
