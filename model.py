# -*- coding: utf-8 -*-
"""
model.py

Created on Mon Jan 14 14:41:17 2019
Updated on Thur Jan 24

@author: David Nicholson

A simple agent based model

Changes:
    - Output of environment to file added
    - Output of total consumption of agents to a file added
    - Made the agents use the entire environment (but not properly error
      checked - yet!)

"""

import csv
import matplotlib.pyplot as plt
import agentframework

num_of_agents = 100
num_of_iterations = 10000
agents = []
rowlist = []
environment = []
rowNum = 0
colNum = 0
colNumList = []

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

# check all rows have same number of columns
def colCheck():

    incorrectCols = []

    for col in colNumList:
        if col == (sum(colNumList) / (len(colNumList))):
            incorrectCols.append(0)
        else:
            incorrectCols.append(1)

    if sum(incorrectCols) != 0:
        return False
    else:
        return True

with open('in.txt', newline='') as file:
    dataset = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowNum += 1
        for values in row:
            rowlist.append(values)
            colNum += 1
        colNumList.append(colNum)
        colNum = 0
        environment.append(rowlist)
        rowlist=[]

#If the columns are all the same length, make the agents
#If not all the same length things get a bit more complicated!
if colCheck():
    # Make the agents.
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, rowNum, colNumList[0]))

    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()


    plt.xlim(0, colNumList[0])
    plt.ylim(0, rowNum)
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x,agents[i].y)
    plt.show()

    # Output environment to a file
    with open('environmentOutput.csv', 'w', newline = '') as file2:
        writer = csv.writer(file2)
        for row in environment:
            writer.writerow(row)

    # Output total units consumed by agents to a file
    with open('agentOutput.txt', 'a') as file3:
        total = 0
        for agent in agents:
            total += agent.store
        file3.write(str(total) + "\n")

