#  Simulation of the plane boarding strategies!

As the title says we are examining various ways how to board an airplane. 

# Files:

## plane.py
## queue.py
## methods.py

In our file "methods" are 8 boarding methods which we use to tests:

 - Random order
 - Back to front
 - Front to back
 - Back to front (4 groups)
 - Front to back (4 groups)
 - Window-middle-aisle
 - Steffen Perfect
 - Steffen "Modified"

## viz.py
This is vizualization file. Simply if u want to see how it works, put all files in one directory and use this command:
>python3  -m  viz.py

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

## runes.py
![](MainPlot.png)
![](Test1.png)
![](Test2.png)
