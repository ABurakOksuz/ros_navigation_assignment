#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
def pose_callback(data):
    rospy.loginfo("Kaplumbaganın Konumu -> X: %f, Y: %f, Z: %f", data.x, data.y, data.theta)

def move():
    rospy.init_node('robot_kontrol_node', anonymous=True)
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        move_msg = Twist()
        move_msg.linear.x = 4.0  
        move_msg.angular.z = 2.0 

        speed_publisher.publish(move_msg)
        
        rospy.loginfo("Hareket komutu gönderildi!")
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
