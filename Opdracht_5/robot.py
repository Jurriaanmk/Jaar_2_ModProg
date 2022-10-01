"""
Definition of the Robot class used for simulating the pose (location and orientation) 
of a robot in 2D.
For use in the practical ModProg, Mechatronics programme, The Hague University of Applied
Sciences.
Creation date: 25/08/2021
License: GNU General Public License (GNU GPLv3)
"""

from math import cos, sin

class Robot:
    
    def __init__(self, pose = None):
        """
        Robot(pose) returns a Robot object where pose is a
        list of three numbers, the first two are the Robot's
        x- and y-coordinate, the third value is the orientation.
        Robot() will return a Robot object with its pose set to
        the default value [0.0, 0.0, 0.0].
        """
        if pose is None:
            pose = [0.0, 0.0, 0.0]
            
        self._pose = pose  # attributes with 1 or 2 underscores (_)
        # before its name are meant in python not to be used from outside the class
        # definition, so are internal to the class. Sometimes called private, but they
        # are not secret.

    def get_pose(self):
        """Returns the pose of the robot."""
        return self._pose

    def set_pose(self, pose = None):
        """Sets the pose of the robot, without argument
        the pose is set to its default value [0.0, 0.0, 0.0]."""
        if pose is None:
            pose = [0.0, 0.0, 0.0]
        self._pose = pose

    def get_location(self):
        """Returns the location of the robot in 2D (first x-, then y-coordinate)."""
        return self._pose[0:2]

    def get_x(self):
        """Returns the x-coordinate of the robot."""
        return self._pose[0]

    def get_y(self):
        """Returns the y-coordinate of the robot."""
        return self._pose[1]

    def get_orientation(self):
        """Returns the orientation of the robot in radians."""
        return self._pose[2]

    def get_xdir(self):
        """Returns the x-part of the robots orientationvector."""
        return cos(self._pose[2])
    
    def get_ydir(self):
        """Returns the y-part of the robots orientationvector."""
        return sin(self._pose[2])

    def get_orientation_vector(self):
        """Returns the orientationvector of the robot."""
        return [self.get_xdir(), self.get_ydir()]

    def forward(self, distance = 0.0):
        """Moves the robot over a distance in the direction of its
        current orientation."""
        #iets met de orientatie vector en de afstand, cos en sin erbij maar zie niet in hoe.
        self.get_x()+self.d
        
        return 
        
        # implement this function yourself
        raise NotImplementedError

    def rotate(self, angle = 0.0):
        """Changes the orientation only, i.e. adds angle to the orientation."""
        # implement this function yourself
        raise NotImplementedError

    def move(self,distance = 0.0, angle = 0.0):
        """First moves in a straight line over distance (forward) and then
        adds angle to its orientation (rotate)."""
        # implement this function yourself
        raise NotImplementedError

    def distance_to(self, other_robot):
        """
        Calculates the distance of the robot to other_robot.
        """
        
        
        # implement this function yourself
        raise NotImplementedError

# uit de class defnition
