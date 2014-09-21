#!/usr/bin/python

# Based on Mindsensors documentation and Lejos source code

import logging
from ev3.ev3dev import Msensor

class TouchMux(Msensor):
    H1 = 4194
    L1 = 3859
    H2 = 3692
    L2 = 3425
    H12 = 3158
    L12 = 2857
    H3 = 2723
    L3 = 2393
    H13 = 2389
    L13 = 2196
    H23 = 2192
    L23 = 1978
    H123 = 1975
    L123 = 1721

    T1 = 1
    T2 = 2
    T3 = 4
    T123 = T1 | T2 | T3

    def __init__(self, port=-1):
        Msensor.__init__(self, port, type_id=16)

    def _mv_to_bits(self,mv):
        touch = 0

        if mv > TouchMux.L1 and mv < TouchMux.H1:
            touch = TouchMux.T1
        elif mv > TouchMux.L2 and mv < TouchMux.H2:
            touch = TouchMux.T2
        elif mv > TouchMux.L12 and mv < TouchMux.H12:
            touch = TouchMux.T1 | TouchMux.T2
        elif mv > TouchMux.L3 and mv < TouchMux.H3:
            touch = TouchMux.T3
        elif mv > TouchMux.L13 and mv < TouchMux.H13:
            touch = TouchMux.T1 | TouchMux.T3
        elif mv > TouchMux.L23 and mv < TouchMux.H23:
            touch = TouchMux.T2 | TouchMux.T3
        elif mv > TouchMux.L123 and mv < TouchMux.H123:
            touch = TouchMux.T1 | TouchMux.T2 | TouchMux.T3
        #else:
            #assert False, "bad reading from touchmux sensor: %s" % mv

        logging.debug("touchmux mv reading %d => %d", mv,touch)
        return touch

    def is_pushed(self, mask=7):
        return self._mv_to_bits(self.value0 + 0) & mask

