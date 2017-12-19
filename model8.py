# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:16:32 2017

@author: University
"""


import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import random


environment = []
num_of_agents = 10
num_of_iterations = 1
agents = []
neighbourhood = 20
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True


with open('in.txt') as f:
    
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    #print (agents[i].x, agents[i-1].x) #prints the x coord of current and previous agent
    

def update (frame_number):
    fig.clear()
    global carry_on
    
    # Move the agents.
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood)
        
    if random.random() < 0.1:
        carry_on = False
        print('stopping condition')
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #(agents[i].x,agents[i].x)
        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 30) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
  

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)


animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()
      
"""        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

"""


