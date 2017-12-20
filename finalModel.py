"""
Agent Based Model for Inroduction to programming, MSc GIS

Code creates agents with locations set from web-sourced data. They move by 1
unit each iteration in a random direction. They interact with an environment 
(a DEM) and each other, by 'consuming' elevation and sharing this with other 
agents. This process is displayed in an animation and results output in a text
file

Author: gy17arj (Adam Johnston) 
"""


### PRELIMINARY SET-UP ###

#Library imports
import matplotlib.backends.backend_tkagg
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import agentframework 
import csv
import matplotlib.animation
import requests
import bs4
import time
from tkinter import messagebox
import datetime

#Starts timer for working out program run time
start_time = time.time()
#start date and time stamp for this current model run
stamp = str(datetime.datetime.now())

#user defined variables
num_of_agents = 10  #number of agents in model
neighbourhood = 20  #The radius for communication between agents
storeMax = 10000  #the agent storage limit for consuming the environment

#create tuples to hold environment and agent data
environment = []
agents = []
fAgents = []

#Animation variables
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True  #used in generator to continue to next frame


### DEFINING THE ENVIRONMENT ###

#Web scraping for agent starting coordinates 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


#access the environment data from csv using csv.reader
with open('in.txt') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #loop through each row in the csv
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist) #add data to the environment iterable


### INITIALISE MODEL AND CHANGE FUNCTIONS ###

# initialise the agents 
for i in range(num_of_agents):
    
    #set the x and y coordinates from the web scraped daa
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    
    #give the agent environment, coordinates and add to list of agents
    agents.append(agentframework.Agent(environment, agents, y, x))


def update (frame_number):
    """
    Function to to move and interact agents with environment for each frame update
    """
    
    fig.clear()
    global carry_on
    global storeMax
    
    
    #This creates a loop to access each individual agent
    for i in range(num_of_agents):
        
        # Move the agents, consume the environment and share with other agents
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood)
        
        #Variable to hold the value of the agent's store
        s = agents[i].store
        
        #if store of agent[i] exceeds the user-defined threshold, finish model
        if s >= storeMax:
            
            carry_on = False #This stops the next gen_function and so the next frame
            print (agents[i].x,agents[i].y, s)
        
        #plot the agent, scaling the size of the point based on the size of the agent store
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, s**0.5, c='b')
        #(agents[i].x,agents[i].x)
    
    #set the plot size and add the environmental data in the background
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.title('Agent Based Model')
    matplotlib.pyplot.imshow(environment)
   
    
def gen_function(b = [0]):
    """
    Generator function to keep running the model until the storeMax threshold
    is met and the carry_on variable == false
    """
    #iteration/frame number
    a = 0
    tEnv= 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    #while the storeMax threshold hasn't been exceeded by an agent
    while carry_on:
        yield a			# Returns control and waits next call.
        a = a + 1       # another iteration/frame
    
    #Everthing below here happens once threshold is reached
    
    #Loop through the final set of agents
    for t in range(num_of_agents):
        #add each agent coord and store to list
        fAgents.append([agents[t].x, agents[t].y, agents[t].store])
        #add agent store to total store, equals environment consumption
        tEnv = tEnv + agents[t].store
    
    # adds the model parameters and results to a log file
    with open('./ABM_log.txt','a') as t:
        t.write('---> START @ ' + stamp + '\n' + '\n' +
                'Parameters:' + '\n' + 
                'No. of Agents:' + str(num_of_agents) + '\n' + 
                'Neighbourhood:' + str(neighbourhood) + '\n' + 
                'Agent max store:' + str(storeMax) + '\n' + '\n' +
                'Results:' + '\n' +
                'Total iterations: ' + str(a) + '\n' +
                'Total environment consumption: ' + str(tEnv) + '\n'                
                'List of Agents final x & y position and store: ' + str(fAgents) + '\n' +
                '\n' + '-> END' + '\n' + '\n' + ' \n')   
            
    # creates a message box with the nnumber of iterations and processing time taken to complete
    messagebox.showinfo(title="ABM Complete", message=("The model ran for", a, 'iterations, taking %s seconds to complete. Please see the ABM_log file for further details' % (time.time() - start_time)))


def run():
    """
    Function to run one iteration of the model
    """
    
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()


### GUI SET-UP ###

#Setting up the GUI to run the model
root = tkinter.Tk() 
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
  
# Just showing menu elements
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)  #When 'run model' is selected, run function starts
    
#keeps looping through program until user interacts with the GUI
tkinter.mainloop()

#You could put events you want to happen here instead of in the gen_function
#but they only happen once the GUI is closed by the user.

