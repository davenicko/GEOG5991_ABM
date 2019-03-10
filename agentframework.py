# -*- coding: utf-8 -*-
"""
agentframework.py

Created on Mon Jan 21 12:43:19 2019

@author: David Nicholson

The agent class for the GEOG5991 practical agent based model.

Each agent contains it's position in the environment, the environment
itself, and how "full" the agent is. The agent moves in a random
direction when the move function is called. When the eat function is
called, if the position in the environment has less than 10 resources
then all resources are taken and added to the agent's store. If there
are greater than 10 resources then 10 are taken and added to the store.
If the agent's store after this consumption is greater than or equal to
100, the total store is removed from the agent and placed on the
current environment coordinate.

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
        '''
        Initialise the agent.

        environment:    A list of lists containing the amount of
                        resources available at each location in the
                        environment.
        rowNum:         The number of rows in the environment, used to
                        wrap the world when the agent moves.
        colNum:         The number of columns in the environment, used
                        to wrap the world when the agent moves.
        '''
        self._x = random.randint(0,colNum)
        self._y = random.randint(0,rowNum)
        self.environment = environment
        self.store = 0
        self.rowNum = rowNum
        self.colNum = colNum

    def __str__(self):
        '''
        When the class is passed to a print this function returns a
        string which describes the location of the agent
        '''
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
        '''
        Move the agent. If the agent moves beyond the boundaries of the
        environment, meve the agent to the opposite boundary. The
        environment is therefore topographically a torus.
        '''
        if random.random() < 0.5:
            self.y = ((self.y + 1) % self.rowNum)
        else:
            self.y = ((self.y - 1) % self.rowNum)

        if random.random() < 0.5:
            self.x = ((self.x + 1) % self.colNum)
        else:
            self.x = ((self.x - 1) % self.colNum)

    def eat(self):
        '''
        Eat resources in the current location. If there are more than
        ten, eat ten. If there are less eat all. The agent has a
        storage limit of 100 and if this is exceeded the store is
        fully emptied into the current location.
        '''
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        if self.environment[self.y][self.x] <= 10:
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            self.store += self.environment[self.y][self.x]
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0

    # The following allows us to limit access to the object variables.
    # Whenever we try to access the variables, the getter, setter and
    # deleter functions are called instead.
    x = property(getx, setx, delx, "The x coordinate")
    y = property(gety, sety, dely, "The y coordinate")
