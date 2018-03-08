#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ('Michael', 'Bob', 'Tracy', ['yunge', 'handsome'])
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# 不能修改元组内不可变的值
#classmates[0] = 'Adam'

# 元组里的列表内容是可变的
classmates[-1][0] = 'liuxinyun'
print('classmates[-1] =', classmates[-1])
