import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

class GambarSpiral(Node):
    def __init__(self):
        super().__init__('gambar_spiral')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.sub = self.create_subscription(Pose, '/turtle1/pose', self.pos_callback, 10)
        self.pos_turtle = Pose()
        time.sleep(1)
        self.gambar_spiral()

    def pos_callback(self, msg):
        self.pos_turtle = msg

    def gambar_spiral(self):
        twist = Twist()
        jari_jari = 0.005
        start_time = time.time()  
        duration = 6

        while time.time() - start_time < duration: 
            twist.linear.x = jari_jari
            twist.angular.z = -2.0
            self.pub.publish(twist)
            jari_jari += 0.05
            time.sleep(0.1)
        
        
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)

        twist.linear.x = 1.0  
        twist.angular.z = 0.5  
        oval_duration = 3 
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)

       
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)
        

        twist.linear.x = 1.0  
        twist.angular.z = 3.3 
        oval_duration = 0.75
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)

        twist.linear.x = 1.0  
        twist.angular.z = 0.25 
        oval_duration = 1.5
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)

        twist.linear.x = 1.0  
        twist.angular.z = 0.05
        oval_duration = 0.1
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)
        
        twist.linear.x = 1.0  
        twist.angular.z = -0.15
        oval_duration = 2.5
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)
        
        twist.linear.x = 2.0  
        twist.angular.z = -0.05
        oval_duration = 1
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)

        twist.linear.x = 2.0  
        twist.angular.z = -0.05
        oval_duration = 0.5
        start_oval_time = time.time()

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)

        jari_jari = 2.0
        start_time = time.time()  
        duration = 3

        while time.time() - start_time < duration: 
            twist.linear.x = jari_jari
            twist.angular.z = -3.0
            self.pub.publish(twist)
            jari_jari -= 0.05
            time.sleep(0.1)

        while time.time() - start_oval_time < oval_duration:
            self.pub.publish(twist)
            time.sleep(0.1)
       
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)
        
        self.pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    gambar = GambarSpiral()
    rclpy.spin(gambar)
    gambar.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
