#!/usr/bin/env

import rospy
from geometry_msgs.msg import Twist
from numpy import random
print("UwU")
t=Twist()
#print("UwU")
g=random.normal(size=(2000,6),scale=0.2)
i=0
def callback(data):
	global i
	#if data.linear.x!=0:
	t.linear.x=data.linear.x*(0.9+g[i][0])
	#if data.linear.y!=0:
	t.linear.y=data.linear.y*(0.9+g[i][1])
	#if data.linear.z!=0:
	t.linear.z=data.linear.z*(0.9+g[i][2])
	#if data.angular.x!=0:
	t.angular.x=data.angular.x*(0.9+g[i][3])
	#if data.angular.y!=0:
	t.angular.y=data.angular.y*(0.9+g[i][4])
	#if data.angular.z!=0:
	t.angular.z=data.angular.z*(0.9+g[i][5])
	i+=1
	rospy.loginfo("subscriber.linear.x = %s", data.linear.x)
	rospy.loginfo("subscriber.linear.y = %s", data.linear.y)
	rospy.loginfo("subscriber.linear.z = %s", data.linear.z)
	rospy.loginfo("publisher.linear.x=%s", t.linear.x)
	rospy.loginfo("publisher.linear.y=%s", t.linear.y)
	rospy.loginfo("publisher.linear.z=%s", t.linear.z)
	
	if i==2000:
		i=0
def gauss():
	pub=rospy.Publisher('noise_vel', Twist, queue_size=10)
	rospy.init_node('gaussian_noise_add', anonymous=True)
	rate=rospy.Rate(10)
	rospy.Subscriber('cmd_vel', Twist, callback)
	
	
	while not rospy.is_shutdown():
		
		pub.publish(t)
		#rospy.loginfo("publisher.linear.x=%s", t.linear.x)
		#rospy.loginfo("publisher.linear.y=%s", t.linear.y)
		#rospy.loginfo("publisher.linear.z=%s", t.linear.z)
		rate.sleep()
	rospy.spin()

if __name__=='__main__':
	try:
		gauss()
	except rospy.ROSInterruptException:
		pass
	

