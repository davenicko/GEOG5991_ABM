# -*- coding: utf-8 -*-
"""
agentframework.py

Created on Mon Jan 21 12:43:19 2019
Modified on Thur Jan 24

@author: David Nicholson

The agent objects

Changes:
    - override the __str__() method to print out agent coordinates
    - Made the agents use the entire environment (but not properly error
      checked - yet!)
    - Made the agents eat all units remaining if number of units <=10
    - Agents now vomit all of thier store is store > 100
"""
import random

class Agent():
    def __init__(self, environment, rowNum, colNum):
        self._x = random.randint(0,colNum)
        self._y = random.randint(0,rowNum)
        self.environment = environment
        self.store = 0
        self.rowNum = rowNum
        self.colNum = colNum

    def __str__(self):
        return "Location = [" + str(self.x) + ", " + str(self.y) + "]"

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
            self.y = ((self.y + 1) % self.rowNum)
        else:
            self.y = ((self.y - 1) % self.rowNum)

        if random.random() < 0.5:
            self.x = ((self.x + 1) % self.colNum)
        else:
            self.x = ((self.x - 1) % self.colNum)

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        if self.environment[self.y][self.x] <= 10:
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            self.store += self.environment[self.y][self.x]
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0

    x = property(getx, setx, delx, "I'm the x coordinate")
    y = property(gety, sety, dely, "I'm the y coordinate")
