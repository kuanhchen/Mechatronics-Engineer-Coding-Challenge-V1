#Title: unit_test.py 
#Author: Kuan Chen 
#Date: 26/12/2022
#Description: The other file is named 'unit_test'. This script utlizes the unittest library from python and has a unit test for each function within the 'robot_simulation' script.

import unittest
from robot_simulation import Robot,  Simulator, square_controller
from collections import deque

class TestRobot(unittest.TestCase): # robot class testing
    def test_get_position(self): # unit test for instantiation of the robot class and spawn locations
        robot = Robot(0, 0)
        self.assertEqual(robot.get_position(), (0, 0))
        robot = Robot(0, 1)
        self.assertEqual(robot.get_position(), (0, 1))
        robot = Robot(1, 0)
        self.assertEqual(robot.get_position(), (1, 0))
        robot = Robot(1, 1)
        self.assertEqual(robot.get_position(), (1, 1))
        robot = Robot(100, 0)
        self.assertEqual(robot.get_position(), (100, 0))
        robot = Robot(0, 100)
        self.assertEqual(robot.get_position(), (0, 100))
        robot = Robot(-0, -100) # not allowed
        self.assertEqual(robot.get_position(), (0, 0))
        robot = Robot(-100, -100) # not allowed
        self.assertEqual(robot.get_position(), (0, 0)) 
    
    def test_enqueue_command(self): # unit test for the queuing of movement for the robot
        robot = Robot(0, 0)
        robot.enqueue_command(0)
        self.assertEqual(robot.queue, deque([0]))
        robot.enqueue_command(1)
        self.assertEqual(robot.queue, deque([0, 1]))
        robot.enqueue_command(2)
        self.assertEqual(robot.queue, deque([0, 1, 2]))
        robot.enqueue_command(3) 
        self.assertEqual(robot.queue, deque([0, 1, 2, 3]))
        robot.enqueue_command(4) # illegal movement
        self.assertEqual(robot.queue, deque([0, 1, 2, 3]))
        robot.enqueue_command(-1) # not allowed 
        self.assertEqual(robot.queue, deque([0, 1, 2, 3]))
        
    
    def test_execute_next_command(self): # unit test for the execution of movement of the robot
        robot = Robot(0, 0, [0, 1, 2, 3])
        self.assertEqual(robot.get_position(), (0, 0))
        robot.execute_next_command()
        self.assertEqual(robot.get_position(), (0, 1))
        robot.execute_next_command()
        self.assertEqual(robot.get_position(), (1, 1))
        robot.execute_next_command()
        self.assertEqual(robot.get_position(), (1, 0))
        robot.execute_next_command()
        self.assertEqual(robot.get_position(), (0, 0))
    
    def test_move(self): # unit test for the actual movement of the robot, including illegal movement
        robot = Robot(0, 0)
        robot.move(2)
        self.assertEqual(robot.get_position(), (0, 0))
        robot.move(3) # illegal movement
        self.assertEqual(robot.get_position(), (0, 0))
        robot.move(0)
        self.assertEqual(robot.get_position(), (0, 1))
        robot.move(3) # illegal movement
        self.assertEqual(robot.get_position(), (0, 1))
        robot.move(1)
        self.assertEqual(robot.get_position(), (1, 1))
        robot.move(2)
        self.assertEqual(robot.get_position(), (1, 0))
        robot.move(2) # illegal movement
        self.assertEqual(robot.get_position(), (1, 0))
        robot.move(3)
        self.assertEqual(robot.get_position(), (0, 0))
      


class TestSimulator(unittest.TestCase): # simulator class testing 
    def test_add_robot(self): # unit test for the addition of robots to the simulation
        simulator = Simulator()
        robot0 = Robot(0, 0)
        simulator.add_robot("robot0", robot0)
        self.assertEqual(simulator.list_robots(), [robot0])
        robot1 = Robot(0, 0) # TODO Not allowed to occupy same grid point should be just robot0 so will need to scan robot list for coords
        simulator.add_robot("robot1", robot1)
        self.assertEqual(simulator.list_robots(), [robot0, robot1]) 
    
    def test_delete_robot(self): # unit test for the deletion of robots from the simulation 
        simulator = Simulator()
        robot0 = Robot(0, 0)
        robot1 = Robot(1, 1)
        simulator.add_robot("robot0", robot0)
        simulator.add_robot("robot1", robot1)
        simulator.delete_robot("robot0")
        self.assertEqual(simulator.list_robots(), [robot1])
        simulator.delete_robot("robot1")
        self.assertEqual(simulator.list_robots(), [])
        simulator.delete_robot("robot0")
        self.assertEqual(simulator.list_robots(), [])
    
    def test_list_robots(self): # unit test for the retrieval of all robot ids in the simulation
        simulator = Simulator()
        robot0 = Robot(0, 0)
        robot1 = Robot(1, 1)
        simulator.add_robot("robot0", robot0)
        simulator.add_robot("robot1", robot1)
        self.assertEqual(simulator.list_robots(), [robot0, robot1])

class TestSquareController(unittest.TestCase): # square controller testing 
    def test_square_controller(self): 
        robot0 = Robot(0, 0)
        square_controller(robot0)
        self.assertEqual(robot0.queue, deque([0, 1, 2, 3]))
    

# run the test
if __name__ == '__main__':
    unittest.main()