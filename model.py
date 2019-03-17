#!/usr/bin/env python3
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
import random
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import agentframework

num_of_agents = 10
num_of_iterations = 1
neighbourhood = 20

# If the correct number of paramaters is passed at the command line
# then change the model parameters to those parameters
try:
    if len(sys.argv) == 4:
        num_of_agents = int(sys.argv[1])
        num_of_iterations = int(sys.argv[2])
        neighbourhood = int(sys.argv[3])
except:
    print("Invalid parameters given. Defaulting to:")
    print("num_of_agents=10")
    print("num_of_iterations = 1")
    print("neighbourhood = 20")
agents = []
row_list = []
environment = []
row_num = 0
col_num = 0
col_num_list = []

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

def update(frame_number):
    '''
    Functon to update the current frame of the animation of the model.
    First the agents move, then they eat, then the current environment
    and agent positions are shown.
    '''
    fig.clear()

    # Shuffle the agents
    random.shuffle(agents)

    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    # Plot the environment and agent positions
    plt.xlim(0, col_num_list[0])
    plt.ylim(0, row_num)
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x, agents[i].y)

# Open the environment file and read into the environment variable
with open('in.txt', newline='') as file1:
    dataset = csv.reader(file1, quoting=csv.QUOTE_NONNUMERIC)
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
    for k in range(num_of_agents):
        agents.append(agentframework.Agent(environment, row_num,
                                           col_num_list[0], agents))

    #Setup the figure
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])

    # Move the agents and show the frame of anmation.
    model_animation = animation.FuncAnimation(fig, update, frames=100,
                                              interval=1, repeat=False)
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

else:
    print("The environment file contains rows that are of differing lengths. "\
          "The model did not run.")
