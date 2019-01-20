# -*- coding: utf-8 -*-
"""
model.py

Created on Mon Jan 14 14:41:17 2019
Updated on Thu Jan 17

@author: David Nicholson

A simple agent based model - initial version to add agents, perform a
rudimentary random walk algorithm and calculate the distance between two
points

Changes:
    - corrected the number for coordinates to be 0-99, not 0-100
    - removed reliance on math by raising to power of 0.5 for sqrt
    - added ability to create any number of agents with a variable
    - added ability to have any number of random walks
    - added a calculation for eastern-most agent
    - added calculation to determine distance between all points with (probably
    ) no duplications
    - we now plot the agents using matplotlib
"""
import random
import operator
import matplotlib.pyplot as plt
import time

agents = []
distances = []
number_of_agents = 100
number_of_walks = 1

def randWalk(val):
    '''
    Move a coordinate by 1 point

    Keyword argument:
    val: the input coordinate (either the x or y coordinate)

    returns:
    the revised coordinate changed by + or - 1
    '''
    if random.random() < 0.5:
        return val + 1
    else:
        return val - 1

def distanceBetween(agent_row_a, agent_row_b):
    '''
    Determine the euclidian distance between two points

    Keyword arguments:
    agent_row_a: first agent
    agent_row_b: second agent

    Returns:
    the euclidian distance between the two using pythagoras' theorem
    '''
    return (((agent_row_a[0]-agent_row_b[0])**2)+((agent_row_a[1]-agent_row_b[1])**2))**0.5


# append to the agents list a random point
for i in range(number_of_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])

# randlomly walk each point 100 times
for i in range(number_of_walks):
    for j in range(number_of_agents):
        agents[j][0] = randWalk(agents[j][0]) % 100
        agents[j][1] = randWalk(agents[j][1]) % 100


# determine the eastern most point of all the agents
eastPoint = max(agents, key=operator.itemgetter(1))

start = time.clock()
# determine the distances betwwen all the agents without duplication*
# *probably
for i in range(len(agents)-1):
    for j in range(len(agents)-i-1):
        distances.append(distanceBetween(agents[i], agents[i+j+1]))
end = time.clock()

print(distances)
print("time taken = " + str(end - start))

# plot the agents
plt.ylim(0, 99)
plt.xlim(0, 99)
for i in range(number_of_agents):
    plt.scatter(agents[i][1], agents[i][0])
plt.scatter(eastPoint[1], eastPoint[0], color='red')
plt.show()
