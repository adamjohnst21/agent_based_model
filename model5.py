# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:16:57 2017

@author: gy17arj
"""

import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agent0, agent1):
    return (((agent0[0] - agent1[0])**2) + ((agent0[1] - agent1[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

agent1 = agentframework.Agent()

print (agent1.y)

agent1.move
print (agent1.y)
# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

"""
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)

"""