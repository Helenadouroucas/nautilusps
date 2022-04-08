#!/usr/bin/env python3
import rospy
import tf2_ros
from random import random
from geometry_msgs.msg import TransformStamped
import math as math

class RandomTransform():
    def __init__(self,nome,raio,veloc):
        rospy.init_node('random_transform', anonymous=True)
        self.tf = TransformStamped()
        self.tf.header.frame_id = 'sol'
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.rotation.w = 1
        self.v = veloc
        self.r = raio
        self.tf.child_frame_id = nome
        self.broadcaster = tf2_ros.TransformBroadcaster()

    
        
    def broadcast(self):

        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.translation.x = self.r * math.sin(((1000000000*self.tf.header.stamp.secs+self.tf.header.stamp.nsecs)/10000000000)*self.v)
        self.tf.transform.translation.y = self.r * math.cos(((1000000000*self.tf.header.stamp.secs+self.tf.header.stamp.nsecs)/10000000000)*self.v)
        self.tf.transform.translation.z = 0


        self.broadcaster.sendTransform(self.tf)

if __name__ == '__main__':
    
    planeta1 = RandomTransform(rospy.get_param('planetas/planeta1/nome'),rospy.get_param('planetas/planeta1/raio'),rospy.get_param('planetas/planeta1/velocidade'))
    planeta2 = RandomTransform(rospy.get_param('planetas/planeta2/nome'),rospy.get_param('planetas/planeta2/raio'),rospy.get_param('planetas/planeta2/velocidade'))
    planeta3 = RandomTransform(rospy.get_param('planetas/planeta3/nome'),rospy.get_param('planetas/planeta3/raio'),rospy.get_param('planetas/planeta3/velocidade'))
    planeta4 = RandomTransform(rospy.get_param('planetas/planeta4/nome'),rospy.get_param('planetas/planeta4/raio'),rospy.get_param('planetas/planeta4/velocidade'))    
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        
        planeta1.broadcast()
        planeta2.broadcast()
        planeta3.broadcast()
        planeta4.broadcast()

        rate.sleep()