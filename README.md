#  Simulation of the plane boarding strategies

The aim of this project it to examine and compare various methods of boarding a plane (16 rows consisting of 6 seats each).
Our implementation is based on ***Mesa*** - an agent-based modeling framework for **Python 3** (more information can be found
on https://mesa.readthedocs.io/).

To work properly, it requires following libraries installed:
 - **mesa** 
 - **numpy**
 - **pandas**
 - **seaborn**
 - **mathplotlib**


# Files:

## plane.py
## queue.py

File "*queue.py*" contains a definition of ***QueueScheduler*** - an extension of *BaseScheduler* delivered by *Mesa*.
Instead of a single agent buffer, the modified version consists of two separate queue - *standard* and *priority*.
Agents placed in priority queue are guaranteed to progress before those in standard one.
Such implementation allows for better control over the flow of simulation, while still being compatible
with most of functions in *Mesa*.

## methods.py

File "*methods.py*" consists of 8 functions representing boarding methods which we are meant to simulate:

 - Random order
 - Back to front
 - Front to back
 - Back to front (4 groups)
 - Front to back (4 groups)
 - Window-middle-aisle
 - Steffen Perfect
 - Steffen "Modified"

## viz.py
This is visualization file. Simply if u want to see how it works, put all files in one directory and use this command:
>python3  -m  viz.py

<<<<<<< HEAD
After this in your browser should show up new tab (resembling an image below):

![](webpage.png)
<br><br>
The left panel consists of three variables:
 - **Boarding method** (allows for choice of the boarding method)
 - **Enable shuffle** (enables and disables suit shuffles)
 - **Luggage size** (an integer from a range from 0 to 7 or a value drawn from normal distribution)

On the right side, there are three buttons controlling the flow of simulation:
 - **Start/Stop** (turns on and pauses the visualization)
 - **Step** (progresses the simulation by one step)
 - **Reset** (clears the board)
=======
After this in your browser should show up new tab(like image below)
![](webpage.png)

On the left side panel are tree variables:

 - Boarding method (chose method which you want to run)
 - Enable shuffle (seat shuffle is enable or not)
 - Luggage size (from 0 to 7 or normal distribution)

On the right side are tree buttons:

 - Start/Stop (simply turn on or off vizualization)
 - Step (does one vizualization step)
 - Reset (clear board)
>>>>>>> ac945cbbfa464513f1da61f8fe0f045d0757d633

## runes.py
![](MainPlot.png)
![](Test1.png)
![](Test2.png)
