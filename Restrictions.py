#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diego Rueda
"""

def rest(cromValue):
    eval = lambda x: x - 42 if x - 42 > 0 else 0
    eval_2 = lambda x,y,z:x+2*y+2*z - 72 if x+2*y+2*z-72 > 0 else 0
    diff_1 = eval(cromValue[0])
    diff_2 = eval(cromValue[1])
    diff_3 = eval(cromValue[2])
    diff_4 = eval_2(cromValue[0],cromValue[1],cromValue[2])
    return [diff_1,diff_2,diff_3, diff_4]
