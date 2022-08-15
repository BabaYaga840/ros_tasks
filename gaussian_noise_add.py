#!/usr/bin/env

import rospy
from geometry_msgs.msg import Twist
from numpy import random

t=Twist()
#print("UwU")
g=random.normal(size=(2000,6))
i=0
def callback(data):
	global i
	t.linear.x=data.linear.x+gii][0]
	t.linear.y=data.linear.y+gii][1]
	t.linear.z=data.linear.z+g[i][2]
	t.angular.x=data.angular.x+g[i][3]
	t.angular.y=data.angular.y+g[i][4]
	t.angular.z=data.angular.z+g[i][5]
	i++
	rospy.loginfo("subscriber.linear.x = %s", t.linear.x)
	rospy.loginfo("subscriber.linear.y = %s", t.linear.y)
	rospy.loginfo("subscriber.linear.z = %s", t.linear.z)
	if i=2000:
		i=0
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
	

