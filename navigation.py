#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyResponse

def go_home(request):
    rospy.loginfo("Going to home.")
    rospy.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def go_to_kitchen(request):
    rospy.loginfo("Going to kitchen.")
    rospy.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def stop(request):
    rospy.loginfo("Stop!")
    return EmptyResponse()

rospy.init_node('navigation_node')
go_home_service = rospy.Service('/go_home', Empty, go_home)
go_to_kitchen_service = rospy.Service('/go_to_kitchen', Empty, go_to_kitchen)
stop_service = rospy.Service('/stop', Empty, stop)

rospy.spin()
