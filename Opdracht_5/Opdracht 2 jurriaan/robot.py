"""
Definition of the Robot class used for simulating the pose (location and orientation) 
of a robot in 2D.
For use in the practical ModProg, Mechatronics programme, The Hague University of Applied
Sciences.
Creation date: 25/08/2021
License: GNU General Public License (GNU GPLv3)
"""
#%%
from math import cos, sin, sqrt
from turtle import position

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
        # implement this function yourself
        """Moves the robot over a distance in the direction of its
        current orientation."""
        distance_x = Robot.get_xdir(self) * distance
        self._pose[0] = self._pose[0] + distance_x
        distance_y = Robot.get_ydir(self) * distance
        self._pose[1] = self._pose[1] + distance_y        
        return
        
        raise NotImplementedError

    def rotate(self, angle = 0.0):
        """Changes the orientation only, i.e. adds angle to the orientation."""
        # implement this function yourself
        self.set_pose ([self.get_x(), self.get_y(), self.get_orientation()+angle])
        
        return 
        raise NotImplementedError

    def move(self,distance = 0.0, angle = 0.0):
        """First moves in a straight line over distance (forward) and then
        adds angle to its orientation (rotate)."""
        # implement this function yourself
        for i in self:
            Robot.forward(i, distance)
            Robot.rotate(i, angle)
    
    def distance_to(self, other_robot):
        """
        Calculates the distance of the robot to other_robot.
        """
        x_pose_self = self._pose[0]
        y_pose_self = self._pose[1]

        
        x_pose_other = other_robot._pose[0]
        y_pose_other = other_robot._pose[1]
        
        x_Distance = x_pose_other - x_pose_self
        y_Distance = y_pose_other - y_pose_self
        return (sqrt(x_Distance**2+y_Distance**2))
    
    
        # implement this function yourself
        raise NotImplementedError
    

# uit de class defnition

#%%

# %%
