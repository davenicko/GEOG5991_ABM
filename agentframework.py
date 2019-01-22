# -*- coding: utf-8 -*-
"""
agentframework.py

Created on Mon Jan 21 12:43:19 2019

@author: David Nicholson

The agent objects

Changes:
    - added the environment to the class, and a method to interact (eat) the 
      environment
"""
import random

class Agent():
    def __init__(self, environment):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def setx(self, value):
        self._x = value

    def sety(self, value):
        self._y = value

    def delx(self):
        del self._x

    def dely(self):
        del self._y

    def move(self):
        if random.random() < 0.5:
            self.sety((self.y + 1) % 100)
        else:
            self.sety((self.y - 1) % 100)

        if random.random() < 0.5:
            self.setx((self.x + 1) % 100)
        else:
            self.setx((self.x - 1) % 100)

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    x = property(getx, setx, delx, "I'm the x coordinate")
    y = property(gety, sety, dely, "I'm the y coordinate")
