#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.subscription = self.create_subscription(Point, '/point', self.point_callback, 10)
        # Temat specyficzny dla Turtlesim
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.height = 512

    def point_callback(self, msg):
        twist = Twist()
        # Logika projektu 3.0: kliknięcie góra/dół ekranu
        if msg.y < self.height / 2:
            twist.linear.x = 2.0  # Jedź do przodu
            self.get_logger().info('Polecenie: PRZÓD')
        else:
            twist.linear.x = -2.0 # Jedź do tyłu
            self.get_logger().info('Polecenie: TYŁ')
        
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()
