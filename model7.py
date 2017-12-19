# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:16:32 2017

@author: University
"""


import matplotlib.pyplot
import agentframework
import csv


def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5


environment = []


with open('in.txt') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


num_of_agents = 10
num_of_iterations = 1
agents = []
neighbourhood = 20

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    #print (agents[i].x, agents[i-1].x) #prints the x coord of current and previous agent
    




# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood)

"""
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()



for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)
"""
