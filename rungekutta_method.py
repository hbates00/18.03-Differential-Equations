# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:59:22 2016

@author: Haley
"""
# ta: initial value of t
# tb: final value of t
# ya: initial value of y
# n : number of steps
# Returns value of y at tb. 

def func(t, y):
    return 3*y*(t**-1) + (t**-4)*(y**2) 

def oneEuler(t, y, h):
    y += h * func(t, y)
    t += h
    return (t, y)

def RungeKutta(ta, tb, ya, n):
    h = (tb - ta) / float(n)
    t = ta
    y = ya
    for i in range(n):
        y += func(((t + oneEuler(t, y, h)[0])/2), ((y + oneEuler(t, y, h)[1])/2)) * h
        t += h
        
        print 't value' + str(t)
        print 'y value' + str(y)
        print '--------'
        
    return y
    
ta = 1 #initial time
tb = 2.5 #final time
ya = .5 #initial y
n = 3 #number of steps

print RungeKutta(ta, tb, ya, n)
