#!/usr/bin/env python3
import sys
import rospy
from burak_package.srv import RectangleArea

def area_client(w, h):
    rospy.wait_for_service('calculate_rectangle_area')
    try:
        calculate_area = rospy.ServiceProxy('calculate_rectangle_area', RectangleArea)
        response = calculate_area(w, h)
        return response.area
    except rospy.ServiceException as e:
        print(f"Servis çağrısı başarısız: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
    else:
        width = 5.0
        height = 4.0

    print(f"İstek gönderiliyor: En={width}, Boy={height}")
    result = area_client(width, height)
    print(f"Sunucudan gelen alan: {result}")
