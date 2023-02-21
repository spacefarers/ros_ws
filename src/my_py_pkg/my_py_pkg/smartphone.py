import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from serial_motor_demo_msgs.msg import MotorCommand


class SmartPhoneNode(Node):
    def __init__(self):
        super().__init__('smartphone')
        self.subscriber_ = self.create_subscription(Joy, "joy", self.callback_robot_news, 10)
        self.get_logger().info("Smartphone has started")
        self.publisher_ = self.create_publisher(MotorCommand, "motor_command", 10)

    def callback_robot_news(self, msg):
        self.publish_news(msg.axes[1], msg.axes[3])

    def publish_news(self, msg1, msg2):
        msg = MotorCommand()
        msg.is_pwm = True
        msg.mot_1_req_rad_sec = msg1*255
        msg.mot_2_req_rad_sec = msg2*255
        print(str(msg.mot_1_req_rad_sec)+" "+str(msg.mot_2_req_rad_sec))
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SmartPhoneNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
