#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角
def triangles():
    N = [1]
    while True:
        yield N     # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break