#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import random

class componentes:
    def __init__(self):
        rospy.init_node('componentes',anonymous=True)
        self.pub = rospy.Publisher('vel_lin_ang',Twist,queue_size=10)
        self.lst = list(range(20))
    
    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            v = Twist()
            v.linear.x = random.choice(self.lst)
            v.linear.y = random.choice(self.lst)
            v.linear.z = random.choice(self.lst)
            v.angular.x = random.choice(self.lst)
            v.angular.y = random.choice(self.lst)
            v.angular.z = random.choice(self.lst)
            rospy.loginfo(v)
            self.pub.publish(v)
            rate.sleep()



if __name__ == '__main__':
    try:
        vel = componentes()
        vel.start()
    except rospy.ROSInterruptException:
        pass