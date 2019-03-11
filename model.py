# -*- coding: utf-8 -*-
"""
model.py

Created on Mon Jan 14 14:41:17 2019

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
row_list = []
environment = []
row_num = 0
col_num = 0
col_num_list = []

def distance_between(agents_row_a, agents_row_b):
    '''
    agents_row_a:   The first agent
    agents_row_b:   The second agent

    returns: The euclidian distance between the two agents
    '''
    return (((agents_row_a.x - agents_row_b.x)**2) +
            ((agents_row_a.y - agents_row_b.y)**2))**0.5

# check all rows have same number of columns
def col_check():
    '''
    Function to check all rows have the same number of columns. I have
    used this to make sure we can consistently move the agents to the
    other side of the "world". If this were not in place it is possible
    that we could get an out of range error. With the data included
    this is not strictly necessary, but I added it here regardless.

    returns:    True if all columns are the same, False otherwise
    '''
    incorrect_cols = []

    for col in col_num_list:
        if col == (sum(col_num_list) / (len(col_num_list))):
            incorrect_cols.append(0)
        else:
            incorrect_cols.append(1)

    if sum(incorrect_cols) != 0:
        return False
    else:
        return True

with open('in.txt', newline='') as file:
    dataset = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        row_num += 1
        for values in row:
            row_list.append(values)
            col_num += 1
        col_num_list.append(col_num)
        col_num = 0
        environment.append(row_list)
        row_list = []

#If the columns are all the same length, make the agents
#If not all the same length things get a bit more complicated!
if col_check():
    # Make the agents.
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, row_num,
                                           col_num_list[0]))

    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()


    plt.xlim(0, col_num_list[0])
    plt.ylim(0, row_num)
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x, agents[i].y)
    plt.show()

    # Output environment to a file
    with open('environmentOutput.csv', 'w', newline='') as file2:
        writer = csv.writer(file2)
        for row in environment:
            writer.writerow(row)

    # Output total units consumed by agents to a file
    with open('agentOutput.txt', 'a') as file3:
        total = 0
        for agent in agents:
            total += agent.store
        file3.write(str(total) + "\n")

