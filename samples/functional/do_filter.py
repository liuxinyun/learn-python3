#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 奇数
def is_odd(n):
    return n % 2 == 1

# 回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

L = range(100)

print(list(filter(is_palindrome, L)))
print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
