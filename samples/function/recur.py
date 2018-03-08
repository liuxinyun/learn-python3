#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# 尾递归
def fact1(n):
    return fact_iter(n,1)
def fact_iter(num, product):
    if num==1:
        return product
    return fact_iter(num-1, num*product)

print('fact(6) = ', fact1(6))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b) # 将上边的n-1个小盘子通过c移动到b
        move(1, a, b, c) # 将最后一个大盘子通过b移动c
        move(n-1, b, a, c) # 将b上的n-1个小盘子通过a移动到c

move(4, 'A', 'B', 'C')
