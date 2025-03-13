import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import String


class DistancePubSub(Node):
    def __init__(self):
        super().__init__('distance_pubsub')
        self.subscription = self.create_subscription(Pose,'/turtle1/pose',self.distance_callback,10)

        self.publisher_ = self.create_publisher(String, '/turtle1/distance', 10)

    def distance_callback(self,msg):
        distance = (msg.x**2 + msg.y**2)**0.5

        msg = String()
        msg.data = f"Distance of turtle from origin is: {distance:0.2f}"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    distance_pubsub = DistancePubSub()
    rclpy.spin(distance_pubsub)
    distance_pubsub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
