#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import cv2
import numpy as np

class InterfaceNode(Node):
    def __init__(self):
        super().__init__('interface_node')
        # Parametr rozmiaru kwadratu (Zadanie 4)
        self.declare_parameter('square_size', 20)
        self.sq_size = self.get_parameter('square_size').value
        
        self.publisher_ = self.create_publisher(Point, '/point', 10)
        self.window_name = "Interfejs Turtlesim"
        self.point = None
        
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_event)
        self.create_timer(0.05, self.timer_callback) # 20 FPS odświeżania okna

    def mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x, y)
            msg = Point(x=float(x), y=float(y), z=0.0)
            self.publisher_.publish(msg)
            self.get_logger().info(f'Kliknięto: {x}, {y}')

    def timer_callback(self):
        # Tworzenie czarnego tła 512x700 (Zadanie 3)
        img = np.zeros((512, 700, 3), np.uint8)
        # Biała linia podziału (h=512, więc środek to 256)
        cv2.line(img, (0, 256), (700, 256), (255, 255, 255), 1)
        
        if self.point:
            cv2.rectangle(img, self.point, 
                          (self.point[0] + self.sq_size, self.point[1] + self.sq_size), 
                          (0, 255, 0), 2)
            
        cv2.imshow(self.window_name, img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = InterfaceNode()
    rclpy.spin(node)
    rclpy.shutdown()
