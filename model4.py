"""
Author Adam Johnston

"""

import random 
import operator
import matplotlib.pyplot
import datetime
import agentframework



def getTimeMS():
    """
    Function for timing the code to run
    """
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)


a = agentframework.Agent()

a.y = 10
print (a.y)



def eucDist(agent1, agent2):
    
    """
    Calculates the Euclidean distance between position1 (x1, y1) 
    and position2 (x2, y2)
    """
    eDist = ((((agent1[0]-agent2[0])**2)+((agent1[1]-agent2[1])**2))**0.5)
    
    return eDist


#begin timer    
start = getTimeMS()



#create a list to store agent coordinates
agents = []

#set the number of agents and iterations
numAgents = 10
numIter = 100

#adds coordinates of 10 agents to agents list
for i in range(numAgents):
    agents.append([random.randint(0,99), random.randint(0,99)])


#repeat agent movement 10 times   
for m in range(numIter):
    
    #move each of the agents once
    for i in range(numAgents):
            
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100   
        
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100 
               
agentDist = []
        
for k in range(len(agents)):
    for i in range(len(agents)):
        
        #only calculate the distance if they've not been calculated previously
        if (i > k):
            
            #use the eucDist function to return distance as integer
            distance = int(eucDist(agents[k], agents[i]))
            
            #add to list the 2 agent's numbers and the distance between them
            agentDist.append([k, i, distance])
            
            #print (k, i, distance) #print k and i to see how this loop works       

#set variable to hold max distance, with no value
maxDist = 0   
for i in range(len(agentDist)):
    
    #If that distance is greater than the current distance...
    if agentDist[i][2] > maxDist:
        
        #...replace the value
        maxDist = agentDist[i][2]
        


#set minimum distance variable to infinity
minDist = float('inf')  
for i in range(len(agentDist)):
    
    #if the distance value is less than the current minDist value...
    if agentDist[i][2] < minDist:
        
        #...replace it with that value
        minDist = agentDist[i][2]
              

for i in range(len(agentDist)):
    
    if agentDist[i][2] == maxDist:
        print ('Agent', agentDist[i][0], 'and Agent', agentDist[i][1], 'are the furthest apart at', agentDist[i][2], 'units')
    elif agentDist[i][2] == minDist:
        print ('Agent', agentDist[i][0], 'and Agent', agentDist[i][1], 'are the closest together at', agentDist[i][2], 'units')

#print the location of each agent and identify the most easterly agent
#print (agents, max(agents, key=operator.itemgetter(1)))

#create the x and y axis
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

#m = max(agents, key=operator.itemgetter(1))
#print ('THIS IS M', m)

for i in range(numAgents):
    
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    #matplotlib.pyplot.scatter(m[1], m[0], color='red')

matplotlib.pyplot.show()


end = getTimeMS()

print("time = " + str((end - start)/1000000) + ' seconds')
"""