#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty

if __name__ == '__main__':
    rospy.init_node('main_node')

    try:
        rospy.wait_for_service('/go_to_kitchen')
        go_to_kitchen = rospy.ServiceProxy('/go_to_kitchen', Empty)
        go_to_kitchen()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % str(e))

    try:
        rospy.wait_for_service('/stop')
        stop = rospy.ServiceProxy('/stop', Empty)
        stop()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % str(e))

    try:
        rospy.wait_for_service('/go_home')
        go_home = rospy.ServiceProxy('/go_home', Empty)
        go_home()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % str(e))

    try:
        rospy.wait_for_service('/stop')
        stop()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % str(e))
