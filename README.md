# The Problem:
<p align="justify">
You are building an simplistic AI agent that is responsible for planning a farm.  The job of the agent is to choose the locations at which to plant two crops, corn and beans.  The natural environment is modeled by a "simulator", which will for our toy exercise have very basic rules, and the agent interacts with the simulator to learn how to best plan the farm.<br />
</p>

# Simulator: 
<p align="justify">
The simulator models a farm that is n x n, where n is a configuration parameter.  In each of the n^2 cells, there can be either a corn plant, a bean plant, or empty soil.  The farm starts at time 0 completely empty.  The simulator simulates time ticking forward one day at a time while an agent (which is described next) can do actions each day such as planting a plant or harvesting a plant.  A corn plant in our simulation takes 90 days to grow from time of planting to time of harvest.  A bean plant in our simulation also takes 90 days.  At the 90 day mark, or thereafter, a plant can be harvested, producing 10 units of food (corn or beans), and the cell that the plant was in becomes empty again.  Since bean plants help corn be more productive, for every bean plant that is in one of the adjacent 8 cells to a corn plant, the corn plant produces one extra unit of food at time of harvest.  That is, if there are 3 bean plants directly adjacent to a corn plant, then the corn plant will produce 13 units of food upon harvest rather than 10.  A bean plant that is not next to a corn plant produces 10 units of food upon harvest, and a bean plant that is adjacent to one or more corn plants produces 15 units of food upon harvest.<br />
</p>

# Agent: 
<p align="justify">
The agent interacts with the simulator as a black box (it does not know the rules for how plants interact) and only is able to do the following: plant corn at (x,y), plant bean at (x,y), or harvest crop at (x,y).  It is told by the simulator if it cannot do an action (for example, if there is already a plant at (x,y) or the plant at that location is not ready for harvest), and if a harvest action is successful it is told how much food was produced.  It can perform zero or more actions on any day.  It must use these responses from the simulator as positive and negative rewards, and learn to pick the best plan it can for where to plant the various plants to maximize the food produced by the farm in 91 days.  <br />
</p>

# Task:
<p align="justify">
Implement a basic simulator that follows the rules above and a Monte-Carlo Tree Search agent that produces a farm plan that maximizes the food produced by the farm.   <br />
</p>

# Assumptions:
<p align="justify">
The following assumptions were taken after reading the problem:<br />  
<ol>
<li> Since the farm simulation is run only for 91 days and all the crops take 90 days to become ready for harvestation, the problem just boils down to finding the best position for various crops on the farm on the first day.</li>
<li> Problem Statement mentions that "It can perform zero or more actions on any day." so, the solution only gives the placement of the crops on the farm and the sequece of the plantation doesn't make a difference.</li>
<li> The solution uses Monte Carlo methods and because of its inherent property to randomize, it produces different solution everytime if the number of iterations isn't significantly big then the farm size.</li>
</ol>
</p>


# Sample Run:

With farm Size of 3, the  farm has 3X3 matrix with 9 locations to crop plants. The Best Solution for this is the following


![Alt text](Farm.png?raw=true)


With the above solution at time 1, the harvest at time 91, would harvest 138 units of food.

# Resources:
http://mcts.ai/