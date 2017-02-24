#!/usr/bin/env python3

from pymoos import pymoos as moos
import time
from math import pi


class MOOS2MorseCoordinates(moos.comms):
    """MOOS2MorseCoordinates MOOS app.
    It converts coordinates from MOOS to coordinates for MORSE

    Attributes:
        moos_community: a string representing the address of the Community
        moos_port:      an interger defining the port
    """

    def __init__(self, moos_community, moos_port,
                    src_prefix = 'NAV', out_prefix = 'MORSE_SET'):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(MOOS2MorseCoordinates, self).__init__()
        self.server = moos_community
        self.port = moos_port
        self.name = 'MOOS2MorseCoordinates'
        self.src_prefix = src_prefix
        self.out_prefix = out_prefix

        self.morse_data = {'x' : 0, 'y' : 0, 'z' : 0, 'yaw' : 0}
        self.moos_data = {'x' : 0, 'y' : 0, 'z' : 0, 'yaw' : 0}

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)
        self.run(self.server, self.port, self.name)

    def __on_connect(self):
        """OnConnect callback"""
        return self.register(self.src_prefix+'_X', 0) and \
                self.register(self.src_prefix+'_Y', 0) and \
                self.register(self.src_prefix+'_Z', 0) and \
                self.register(self.src_prefix+'_YAW', 0)

    def __on_new_mail(self):
        """OnNewMail callback"""
        for msg in self.fetch():
            if msg.key() == self.src_prefix+'_X':
                self.moos_data['x'] = msg.double()
            elif msg.key() == self.src_prefix+'_Y':
                self.moos_data['y'] = msg.double()
            elif msg.key() == self.src_prefix+'_Z':
                self.moos_data['z'] = msg.double()
            elif msg.key() == self.src_prefix+'_YAW':
                self.moos_data['yaw'] = msg.double()
        self.ned2enu(self.moos_data, self.morse_data)
        self.publish_data()
        return True

    def ned2enu(self, moos_data, morse_data):
        morse_data['x'] = moos_data['x']
        morse_data['y'] = moos_data['y']
        morse_data['z'] = - moos_data['z']
        morse_data['yaw'] = pi/2. + moos_data['yaw']

    def publish_data(self):
        self.notify(self.out_prefix+'_X', self.morse_data['x'])
        self.notify(self.out_prefix+'_Y', self.morse_data['y'])
        self.notify(self.out_prefix+'_Z', self.morse_data['z'])
        self.notify(self.out_prefix+'_YAW', self.morse_data['yaw'])


def main():
    pinger = MOOS2MorseCoordinates('localhost', 9001)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
