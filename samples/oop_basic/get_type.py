#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))
print('type(123)==int ?', type(123)==int)
print('type(\'abc\')==str ?', type('abc')==str)

import types

print('type(abs)==BuiltinFunctionType ?', type(abs)==types.BuiltinFunctionType)
print('type(lambda x: x)==LambdaType ?', type(lambda x: x)==types.LambdaType)
print('type((x for x in range(10)))==GeneratorType ?', type((x for x in range(10)))==types.GeneratorType)



