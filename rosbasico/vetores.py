#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
#from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32
 
class vetor():
    def __init__(self):
        rospy.init_node('vetor', anonymous=True)
        rospy.Subscriber('vel_lin_ang', Twist, self.callback)
        self.publin = rospy.Publisher('resultlin',Float32,queue_size=10)
        self.pubang = rospy.Publisher('resultang',Float32,queue_size=10)

    def callback(self,msg):
        xl, yl, zl = msg.linear.x, msg.linear.y, msg.linear.z
        vetlin = (xl**2+yl**2+zl**2)**(1/2)
        modlin = Float32()
        modlin.data = vetlin
        self.publin.publish(modlin)

        xa, ya, za = msg.angular.x, msg.angular.y, msg.angular.z
        vetang = (xa**2+ya**2+za**2)**(1/2)
        modang = Float32()
        modang.data = vetang
        self.pubang.publish(modang)
     



if __name__ == '__main__':
    v = vetor()
    rospy.spin()