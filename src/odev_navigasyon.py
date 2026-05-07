#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def hedefe_git(x, y):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo(f"Hedefe gidiliyor... Koordinatlar: x={x}, y={y}")
    client.send_goal(goal)
    
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Hedefe ulaşılamadı!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('odev_5_nokta_node')
        
        noktalar = [
            (0.5, 0.5),
            (1.0, 0.0),
            (1.5, -0.5),
            (0.0, -1.0),
            (-0.5, 0.0)
        ]

        for i, p in enumerate(noktalar):
            rospy.loginfo(f"Nokta {i+1} başlatılıyor...")
            hedefe_git(p[0], p[1])
            rospy.loginfo(f"Nokta {i+1} tamamlandı. 3 saniye bekleniyor...")
            rospy.sleep(3) # Her nokta arasında 3 saniye bekleme
            
        rospy.loginfo("Ödev bitti! Tüm noktalara başarıyla gidildi.")

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigasyon iptal edildi.")
