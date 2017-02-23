from morse.builder import *

def_freq = 60
timewarp = 1
freq = def_freq / timewarp

mokai1 = Robot('mokai.blend')
mokai1.frequency(freq)
mokai2 = Robot('mokai.blend')
mokai2.translate(0,3,0)
mokai2.frequency(freq)

heron = Robot('heron.blend')
heron.frequency(freq)
heron2 = Robot('heron.blend')
heron.translate(3,0,0)
heron2.translate(3,3,0)
heron2.frequency(freq)


# print('NoGravity=',robot.get_properties())

env = Environment('pavlab.blend', fastmode = True)
# env = Environment('water-1/water_scene')

env.set_camera_clip(clip_end=1000)
env.set_camera_speed(15.)
env.set_camera_location([50,0,60])
env.set_camera_rotation([.7,0,1.57])
env.set_camera_focal_length(15.0)

env.simulator_frequency(freq)
env.set_time_scale(timewarp)
env.use_vsync('OFF')
env.use_internal_syncer()
