01110111 01110111 01110111 00101110 01101011 01110101 01100001 01101110 01101000 01100011 01101000 01100101 01101110 00101110 01100011 01101111 01101101
Title: Mechatronics Engineer Coding Challenge V1
Language: Python
Author: Kuan Chen
Date: 26/12/2022
Github Repository: https://github.com/kuanhchen/Mechatronics-Engineer-Coding-Challenge-V1

Description: Contained within are a set of 'extremely simple' simulations for a set of 'turtlebot' style robots. 
Within this folder are two python files. 

One named 'robot_simulation' is the primary library which implements a set of 'turtlebot' style robots. It contains two classes 'Robot' and 'Simulator' 
alongside some helpful functions. The robot class is responsible for creating 'Robot' objects which can perform movement actions as well as reporting 
on a robot's current position. The simulator class is responsible for creating a 'Simulation' in which robots can be added, deleted, and viewed as well 
as perform their movement commands.

The other file is named 'unit_test'. This script utlizes the unittest library from python and has a unit test for each function within the 'robot_simulation' 
script.

Notes on design decisions:
List vs. Deque for commands 
	- As this needed to be a FIFO queue, there were two paths to take. Using a list and 'popping' form the start has a time complexity of O(n) where as 
	using deque and using popleft has a time complexity of O(1). This may not mean alot for small amounts of queue commands, however as the queue size 
	grows this will only get worse and worse. 
Each grid cell containing one robot at a time
	- I couldn't find a nice way to do this. The main way I tried was to implement a check within the run_simulation function which would get the position 
	of the robot moving and forecast its next position. I would then compare that to the current locations of all robots in the simulation and determine
	if the move was valid or not. Something like this:
 	        """ curr_pos = robot_list[k].get_position()
                print(curr_pos)
                if robot_list[k].queue[0] == 0:
                    fut_pos = curr_pos[1] + 1
                elif robot_list[k].queue[0] == 1:
                    fut_pos = curr_pos[0] + 1
                elif robot_list[k].queue[0] == 2:
                    fut_pos = curr_pos[1] - 1
                elif robot_list[k].queue[0] == 3:
                    fut_pos = curr_pos[0] - 1
                print(fut_pos) 
		for j in range(1, len(robot_list))
		    if: fut_pos == robot_list[j].queue[0]
	            	print("Sorry, a robot already occupies that space!")
		    else:
			robot_list[k].execute_next_command() """

Given Assumptions:
- The robots exist within a discrete, finite (NxN) grid; each grid cell may only contain one robot at a time.
- It takes each robot a non-zero period of time to travel between grid cells; during this period, assume the robot occupies both the source and
	destination cell.
- Movement is limited to N/E/S/W directions; no diagonal movement.

My Assumptions:
- No obstacles
- No negative grid locations (i.e -1, -1)
- Ideal simulation conditions
	- Perfect motors & feedback(position)
		-No over/under-shoot, no backlash, perfect grip
- No communications delay
- No external environmental factors affecting travel and communication
	- No wind, uneven surfaces, other external forces
	- No EMI
- Omni-directional wheels (no need to rotate)

How to Run: 
- Ensure you have python installed
- Navigate to this folder in cmd prompt
- Type 'python unit_test.py'
- Otherwise to use the robot_simulation.py 'library' type at the top of your python file
	'from robot_simulation' and 'import' the classes and functions you need

Thank you for this fun project! Have a great new year!
01110111 01110111 01110111 00101110 01101011 01110101 01100001 01101110 01101000 01100011 01101000 01100101 01101110 00101110 01100011 01101111 01101101