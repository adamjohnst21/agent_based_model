# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:46:52 2017

@author: University
"""
import random




class Agent():
    
    """
    Contains objects to initialise and control agents
    """
    
    def eucDist(self, a):
        """
        Calculates the euclidean distance between self and a
        """
        return (((self.x - a.x)**2) + ((self.y - a.y)**2))**0.5
        
    
    def __init__(self, environment, agents, y, x):
        """
        Creates an agent
        """
    
        self.environment = environment #sets the agent's environment to environment
        self.agents = agents 
        self.store = 0
        
        # If no x/y is found from the web scrape, set it to a random integer between 0 and 99
        if x == None:
            self.x = random.randint(0,99)
        else:
            self.x = x
            
        if y == None:
            self.y = random.randint(0,99)
        else:
            self.y = y
            
       
    
    def move(self):
        """
        Moves the agent randomly by 1 unit
        """
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100   
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100 
    
    
    def eat(self): 
        """
        Agent interacts (consumes) with the environment
        """
        #If the environment at that point has at least 10 units
        if self.environment[self.y][self.x] > 10: 
            
            #Calculates and assigns 10% of the environment at that position
            share = ((self.environment[self.y][self.x])*0.1)
            self.environment[self.y][self.x] -= share #remove 10% from the environment
            self.store += share # add the 10% to that agent's store
            
    def share_with_neighbourhood(self, neighbourhood):
        """
        allows agents to interact with each other by sharing stores
        """
        
        # Loop through the agents in self.agents .
        for a in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.eucDist(a) 
            # The agents are within the eighbourhood radius set
            if distance <= neighbourhood:
                
                # calculate the average store 
                sum = (self.store + a.store)
                averageStore = (sum / 2)
                
                # assign this to both agents
                self.store = averageStore
                a.store = averageStore
              
        
        
        
        
        
        
        
        
