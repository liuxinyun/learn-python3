#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

def age():
    age = int(input('请输入你的年龄: '))
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')
age()

def bmi():
    weight = float(input('请输入你的体重：'))
    height = float(input('请输入你的身高：'))

    bmi = weight/height/height
    if bmi < 18.5:
        print('过轻')
    elif bmi < 25:
        print('正常')
    elif bmi < 28:
        print('过重')
    elif bmi < 32:
        print('肥胖')
    else:
        print('严重肥胖')

bmi()





