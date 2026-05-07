#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Hedefe gitme fonksiyonu
def hedefe_git(x, y):
    # move_base istemcisini başlatıyoruz
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Hedef mesajını oluşturuyoruz
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Koordinatları belirliyoruz
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    # Robotun durduğundaki bakış açısı (Quaternion)
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo(f"Hedefe gidiliyor... Koordinatlar: x={x}, y={y}")
    client.send_goal(goal)
    
    # Sonuç gelene kadar bekle
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Hedefe ulaşılamadı!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        # ROS düğümünü başlat
        rospy.init_node('odev_5_nokta_node')
        
        # Buradaki koordinatları RViz'den bakarak kendi haritana göre güncelleyebilirsin
        # (x, y) şeklinde 5 nokta
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
