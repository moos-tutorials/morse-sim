from morse.builder import *

robot = Robot('mokai.blend')


# print('NoGravity=',robot.get_properties())

env = Environment('pavlab.blend')
# env = Environment('water-1/water_scene')
env.set_camera_clip(clip_end=1000)
env.set_camera_location([50,0,60])
env.set_camera_rotation([.7,0,1.57])
env.set_camera_focal_length(15.0)
