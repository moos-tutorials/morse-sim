from morse.builder import *

class Heron(Robot):
    """
    A template robot model for heron, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # heron.blend is located in the data/robots directory
        Robot.__init__(self, 'pavlab_sim/robots/heron.blend', name)
        self.properties(classpath = "pavlab_sim.robots.heron.Heron")

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        self.motion = MotionVW()
        self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            keyboard.properties(ControlType = 'Position')
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)
