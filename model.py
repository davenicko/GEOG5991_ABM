# -*- coding: utf-8 -*-
"""
model.py

Created on Mon Jan 14 14:41:17 2019
Updated on Mon Jan 14

@author: David Nicholson

A simple agent based model - initial version to add agents, perform a
rudimentary random walk algorithm and calculate the distance between two
points
"""
import random
import math

agents=[]

def randWalk(val):
    '''
    Function to move a coordinate by 1 point
    val: the input coordinate (either the x or y coordinate)
    returns the revised coordinate changed by + or - 1
    '''
    if random.random() < 0.5:
        return val + 1
    else:
        return val - 1

def distanceBetween(y0, x0, y1, x1):
    '''
    Determines the euclidian distance between two points
    y0: y coordinate of point 0
    x0: x coordinate of point 0
    y1: y coordinate of point 1
    x1: x coordinate of point 1
    returns the euclidian distance between the two using pythagoras' theorem
    '''
    return math.sqrt(((x1-x0)**2)+((y1-y0)**2))

def startPos():
    '''
    Function to randomise starting positions of points
    Takes no arguments
    Returns a random value between 0 and 99
    '''
    return random.randint(0,100)

#initialise starting positions of the points
y0, x0 = startPos(), startPos()
y1, x1 = startPos(), startPos()

agents.append([y0, x0])

#randlomly walk each point 100 times
for i in range(100):
    y0 = randWalk(y0)
    x0 = randWalk(x0)
    y1 = randWalk(y1)
    x1 = randWalk(x1)

print ("distance between points = ", distanceBetween(y0, x0, y1, x1))
