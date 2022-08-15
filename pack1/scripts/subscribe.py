#!/usr/bin/env
import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo("Recieved: %s", data.data)

def listen():
	rospy.init_node('subscribe', anonymous=True)
	rospy.Subscriber('topic-1', String, callback)
	rospy.spin()

if __name__=='__main__':
	try:
		listen()
	except rospy.ROSInterruptException:
		pass
		
