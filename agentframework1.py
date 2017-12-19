# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:46:52 2017

@author: University
"""
import random




class Agent():
    
    
    def eucDist(self, a):
        return (((self.x - a.x)**2) + ((self.y - a.y)**2))**0.5
        
    
    def __init__(self, environment, agents, y, x):
        
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
    
    def move(self):
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100   
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100 
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbourhood(self, neighbourhood):
        # Loop through the agents in self.agents .
        for a in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.eucDist(a) 
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                sum = (self.store + a.store)
                # Divide sum by two to calculate average.
                averageStore = (sum / 2)
                # self.store = average
                self.store = averageStore
                a.store = averageStore
                    # agent.store = average
                #print("sharing " + str(distance) + " " + str(averageStore))
            # End if
        # End loop
        
        
        
        
        
