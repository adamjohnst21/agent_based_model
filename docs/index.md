---
title: ABM
---

*Navigation:*

[Home](https://adamjohnst21.github.io/website/) --- [ABM](https://adamjohnst21.github.io/agent_based_model/)




# Agent Based Model



Output | Link
--|--
Final Model | [ABM](https://github.com/adamjohnst21/agent_based_model/blob/master/finalModel.py)
Adjoining framework | [Framework](https://github.com/adamjohnst21/agent_based_model/blob/master/agentframework.py)




Blah blah blah, agent based model intro 

**input image of the model**

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
\
\
\
\
\




[![linkedinLogo](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/linkedin.png?raw=true)](https://www.linkedin.com/in/adamjohnstonuk/) [![TwitterLogo](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/twitter.jpg?raw=true)](https://twitter.com/adamjohnst21) [![GitLogo](https://github.com/adamjohnst21/agent_based_model/blob/master/docs/git.png?raw=true)](https://github.com/adamjohnst21)
