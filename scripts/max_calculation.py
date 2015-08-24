#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

# Copyright (C) 2015 General Interfaces GmbH
# Maintainer: Raphael Dürscheid <mailto:rd@gi.ai>

# This file is part of *Test the coder*.

# *Test the coder* is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# *Test the coder* is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with *Test the coder*.  If not, see <http://www.gnu.org/licenses/>.

import rospy
from numpy import random
from programming_test.msg import Solution
from std_msgs.msg import Int64
import numpy as np

class running_maximum:
    	"""calculate the running maximum for a given window"""
	def __init__(self, windowsize):
        	self.array = np.zeros(windowsize)

	def put(self, number_in):
        	np.put(self.array, [0], [number_in])
        	self.array = np.roll(self.array,1)
        	return True

	def get(self):
        	return np.amax(self.array)

def talker(data):
	print data
	pub2 = rospy.Publisher('max_calculation', Solution, queue_size=10)
	msg = Solution()

	rate = rospy.Rate(100) # 100hz
	## put random number into "input (uint64)"
	msg.input = data.data
	## calculate max value as solution (int64)
	r_max.put(msg.input)
	msg.solution = r_max.get()
		
        rospy.loginfo(msg) ## print msg in shell
        pub2.publish(msg)
        rate.sleep()

def callback(data):
	talker(data)

# set window size to be 1000
r_max = running_maximum(1000) 

def listener():		

    	rospy.init_node('calculation')
    	rospy.Subscriber("numbers", Int64, callback)
	rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
