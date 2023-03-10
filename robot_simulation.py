#Title: robot_simulation.py 
#Author: Kuan Chen 
#Date: 26/12/2022
#Description: This script contains two classes 'Robot' and 'Simulator' alongside some helpful functions. The robot class is responsible for creating 
# 'Robot' objects which can perform movement actions as well as reporting on a robot's current position. The simulator class is responsible for creating 
#  a 'Simulation' in which robots can be added, deleted, and viewed as well as perform their movement commands.

# TODO  each grid cell may only contain one robot at a time. It takes each robot a non-zero period of time to travel between grid cells; during this period, assume the robot occupies both the source and
# destination cell.
    
from collections import deque

NORTH = 0 # variables tying compass directions to integers  
EAST = 1 
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, x=0, y=0, queue=None): # creates an instantiation of the robot class, spawns at default 0, 0 unless otherwise specified 
        if x<0 or y<0: # catch case for neagtive spawn coordinates 
            print("Sorry this is not allowed, we don't want the robot to spawn off of the board!")
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y
        self.queue = deque(queue) if queue else deque()
    
    def get_position(self): # returns the position of the robot instance 
        return self.x, self.y 
    
    def enqueue_command(self, direction): # queues a directional command to a double ended queue
        if direction>3 or direction<0: # catch case for invalid movement commands 
            print("Sorry, illegal movement!")
        else:
            self.queue.append(direction)
    
    def execute_next_command(self): # allows for execution of the queue according to a fifo basis 
        #likely implement queue checking here
        try:
            direction = self.queue.popleft()
            self.move(direction)
        except IndexError: # catches index errors based on empty deques 
            pass
    
    def move(self, direction): # facilitates the actual movement of the robot
        if direction == NORTH:
            self.y += 1
        elif direction == EAST:
            self.x += 1
        elif direction == SOUTH:
            if self.y != 0: # includes two catch cases for invalid movement commands based on current coordinates 
                self.y -= 1
            else:
                print("Sorry this is not allowed, we don't want the robot to drive off of the board!") 
        elif direction == WEST:
            if self.x != 0:
                self.x -= 1
            else:
                print("Sorry this is not allowed, we don't want the robot to drive off of the board!")

class Simulator:
    def __init__(self): # creates an instantiation of the simulator class, it has 0 robots by default 
        self.robots = {}
    
    def add_robot(self, id, robot): # allows for the addition of robots into the simulator
        if len(self.robots) == 0: # no robots, allow for any coordinate
            self.robots[id] = robot
        else: # otherwise check if there is a robot occupying the space
            for l in range(0, len(self.robots)):
                if (robot.x, robot.y) == self.robots[l].get_position():
                    print("There is a robot already occupying this coordinate")
                else:
                    self.robots[id] = robot
    
    def delete_robot(self, id): # allows for the deletion of robots from the simulator
        if len(self.robots) == 0:
            print("Sorry, no more robots left!")
        else: 
            del self.robots[id]
    
    def list_robots(self): # shows the current robots in the simulation
        return list(self.robots.values())
    

def square_controller(robot): # robot controller queuing a robot in a 1x1 square pattern
    for i in range(0, 4):
        robot.enqueue_command(i) 

def run_simulation(simulator, timesteps): # runs the simulation for a user specified time
    robot_list = simulator.list_robots()
    for t in range(timesteps):
        if robot_list == []: # catch case for no robots in the simulation
            print("No robots to move")
        else:   
            for k in range(0, len(robot_list)):
                #catch case here for the TODO
                robot_list[k].execute_next_command() 