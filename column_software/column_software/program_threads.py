# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:51:31 2016

@author: Jonathan
"""

import threading
import time


class update_time(threading.Thread):
    """ a test thread that adds the time to data 10 times
    
    data -- output list for prints (default empty)
    delay -- timer delay between cloack reads (default 5)"""

    def __init__ (self, data=[], delay=5):
        threading.Thread.__init__(self)
        self.delay = delay
        self.data = data

    def run(self):
        for x in range(1,10):
            tm = time.gmtime()
            self.data.append("The time is {}:{}:{}".format(tm.tm_hour, tm.tm_min, tm.tm_sec))
            time.sleep(self.delay)