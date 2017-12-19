# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:16:32 2017

@author: University
"""
#import matplotlib.backends.backend_tkagg
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import random
import requests
import bs4

environment = []
num_of_agents = 10
num_of_iterations = 50
agents = []
neighbourhood = 20
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
storeMax = 0


r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

with open('in.txt') as f:
    
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    #print (agents[i].x, agents[i-1].x) #prints the x coord of current and previous agent
    

def update (frame_number):
    fig.clear()
    global carry_on
    global storeMax
    # Move the agents.
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood)
        
    if random.random() < 0.1:
        carry_on = False
        print('stopping condition')
        
    for i in range(num_of_agents):
        s = agents[i].store
        if s >= 500:
            storeMax = 1
            print (agents[i].x,agents[i].y, s)
        
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, s, c='b')
        #(agents[i].x,agents[i].x)
        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
     
def gen_function(b = [0]):
    a = 0
    global storeMax
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (storeMax == 0) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

root = tkinter.Tk() 
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
  
# Just showing menu elements
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)  
    
tkinter.mainloop()





