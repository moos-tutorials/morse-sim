#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <pavlab_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from pavlab_sim.builder.robots import Mokai
import argparse

robot = Mokai()
robot.set_moos(moos_port=9001)
robot.translate(1.0, 0.0, 0.0)
robot.rotate(0.0, 0.0, 3.5)


# set 'fastmode' to True to switch to wireframe mode
env = Environment('water-1/deep_water', fastmode = False)

water = bpymorse.get_object('Water')
water.scale = [500.0, 500.0, 0.0]

env.set_horizon_color([0, .6, 1])
env.set_camera_location([10.0, -10, 10])
env.set_camera_rotation([1.09, 0, .78])
env.set_camera_clip(clip_end=1000)
env.set_camera_focal_length(15.0)
env.set_camera_speed(15.)


new_arglist = sys.argv[sys.argv.index('--')+1:]
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--timewarp', type=int, help='timewarp (speed-up) of simulation',
    default=1)
args = parser.parse_args(new_arglist)
timewarp = args.timewarp
def_freq = 20.
freq = def_freq / timewarp
robot.frequency(freq)
env.simulator_frequency(freq)
env.set_time_scale(timewarp)
env.use_vsync('OFF')
env.use_internal_syncer()
