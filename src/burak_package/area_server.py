#!/usr/bin/env python3
import rospy
from burak_package.srv import RectangleArea, RectangleAreaResponse

def handle_calculate_area(req):
    area = req.width * req.height
    print(f"Hesaplanıyor: {req.width} x {req.height} = {area}")
    return RectangleAreaResponse(area)

def area_server():
    rospy.init_node('rectangle_area_server') 
    s = rospy.Service('calculate_rectangle_area', RectangleArea, handle_calculate_area)
    print("Alan hesaplama servisi hazır...")
    rospy.spin()

if __name__ == "__main__":
    area_server()
