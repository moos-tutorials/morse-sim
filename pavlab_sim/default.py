#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <pavlab_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from pavlab_sim.builder.robots import Mokai

# Add the MORSE mascott, MORSY.
# Out-the-box available robots are listed here:
# http://www.openrobots.org/morse/doc/stable/components_library.html
#
# 'morse add robot <name> pavlab_sim' can help you to build custom robots.
robot = Mokai()
robot.set_moos(moos_port=9001)

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
robot.translate(1.0, 0.0, 0.0)
robot.rotate(0.0, 0.0, 3.5)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> pavlab_sim' can help you with the creation of a custom
# actuator.
#motion = MotionVW()
#robot.append(motion)


# Add a keyboard controller to move the robot with arrow keys.
#keyboard = Keyboard()
#robot.append(keyboard)
#keyboard.properties(ControlType = 'Position')

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> pavlab_sim' can help you with the creation of a custom
# sensor.
#pose = Pose()
#robot.append(pose)

# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html
# the other available interfaces (like ROS, YARP...)
# robot.add_stream('moos')


# set 'fastmode' to True to switch to wireframe mode
env = Environment('water-1/deep_water', fastmode = False)

water = bpymorse.get_object('Water')
water.scale = [500.0, 500.0, 0.0]

env.set_horizon_color([0, .6, 1])
env.set_camera_location([10.0, -10, 10])
env.set_camera_rotation([1.09, 0, .78])
env.set_camera_clip(clip_end=1000)
