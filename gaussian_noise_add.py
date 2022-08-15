#!/usr/bin/env

import rospy
from geometry_msgs.msg import Twist
from numpy import random

t=Twist()
print("UwU")
def callback(data):
	g=random.normal(size=(2,3))
	t.linear.x=data.linear.x+g[0][0]
	t.linear.y=data.linear.y+g[0][1]
	t.linear.z=data.linear.z+g[0][2]
	t.angular.x=data.angular.x+g[1][0]
	t.angular.y=data.angular.y+g[1][1]
	t.angular.z=data.angular.z+g[1][2]
	
	rospy.loginfo("subscriber.linear.x = %s", t.linear.x)
	rospy.loginfo("subscriber.linear.y = %s", t.linear.y)
	rospy.loginfo("subscriber.linear.z = %s", t.linear.z)
	
def gauss():
	pub=rospy.Publisher('noise_add', Twist, queue_size=10)
	rospy.init_node('gaussian_noise_add', anonymous=True)
	rate=rospy.Rate(10)
	
	rospy.Subscriber('cmd_vel', Twist, callback)
	
	while not rospy.is_shutdown():
		pub.publish(t)
		rospy.loginfo("publisher.linear.x=%s", t.linear.x)
		rospy.loginfo("publisher.linear.y=%s", t.linear.y)
		rospy.loginfo("publisher.linear.z=%s", t.linear.z)
		rate.sleep()
		
	rospy.spin()

if __name__=='__main__':
	gauss()
	

