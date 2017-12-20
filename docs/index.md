---
title: ABM
---

*Navigation:*

[Home](https://adamjohnst21.github.io/website/) --- [ABM](https://adamjohnst21.github.io/agent_based_model/)




# Agent Based Model
 
 
### Scripts:
Output | Link
--|--
Final Model | [ABM](https://github.com/adamjohnst21/agent_based_model/blob/master/finalModel.py)
Adjoining framework | [Framework](https://github.com/adamjohnst21/agent_based_model/blob/master/agentframework.py)
 
 
### Introduction
 
This agent based model (ABM) creates a user defined number of agents which are able to move randomly. As they move, they are able to interact with their environment. This environment is a DEM, accessed from a CSV file. The agents consume 10% of the elevation at each point as they move, which accumulates in thier store. Agents interact with each other by sharing their store with other agents within a user defined radius (neighbourhood). Once an agent reaches a user defined maximum store value, the model is complete and stops running. 

The model is initiated and displayed in a GUI. The Model is animated, with each frame representing one iteration of movement and interaction of the set of agents. Once complete, the model parameters and results are added to a ABM_log.txt file, so a user can track and compare past runs of the program. 
 
 
### Example final model
 
![model](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/fModel.PNG?raw=true)
*ABM with 10 agents and a maximum store of 10,000*
 
 
### Common issue
```python

  File "C:/Users/University/Documents/Programming/adamjohnst21.github.io/agent_based_model/model9.py", line 96, in <module>
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

AttributeError: module 'matplotlib.backends' has no attribute 'backend_tkagg'
``` 
The above attribute error was common when using spyder on my personal computer. I found the solution to be the below import. I'm not convinced this is a solid solution, but in keeping with the general python ethos, good enough is just that.

```python
import matplotlib.backends.backend_tkagg #it is this import that seemed to fix the error
import matplotlib
matplotlib.use('TkAgg')
``` 
 
 
[![linkedinLogo](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/linkedin.png?raw=true)](https://www.linkedin.com/in/adamjohnstonuk/) [![TwitterLogo](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/twitter.jpg?raw=true)](https://twitter.com/adamjohnst21) [![GitLogo](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/git.png?raw=true)](https://github.com/adamjohnst21)
