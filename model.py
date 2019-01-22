# -*- coding: utf-8 -*-
"""
model.py

Created on Mon Jan 14 14:41:17 2019
Updated on Tue Jan 22

@author: David Nicholson

A simple agent based model

Changes:
    - Added the environment
    - Added a call to the interaction method
    - Added code to display the agents and environment
"""

import csv
import matplotlib.pyplot as plt
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 100
num_of_iterations = 1000
agents = []
rowlist = []
environment = []

with open('in.txt', newline='') as file:
    dataset = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        for values in row:
            rowlist.append(values)
        environment.append(rowlist)
        rowlist=[]

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()


plt.xlim(0, 99)
plt.ylim(0, 99)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b)

plt.imshow(environment)
plt.show()
