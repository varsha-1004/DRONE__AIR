import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

sensor_id=0
capture_width=1280
capture_height=720
framerate=120
flip_method=0
display_width=640
display_height=480

class Ros_Camera(Node):
    def __init__(self):
        super().__init__('Camera_Publisher')
        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
        timer_period=0.01
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.video_capture= cv2.VideoCapture("nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        ), cv2.CAP_GSTREAMER)
        self.br=CvBridge()

      
    def timer_callback(self):
        ret,frame=self.video_capture.read()
        if ret==True:
            self.publisher_.publish(self.br.cv2_to_imgsmg(frame))
        self.get_logger().info("Publishing")

def main(args=None):
  
    # Initialize the rclpy library
        rclpy.init(args=args)
    
    # Create the node
        image_publisher = Ros_Camera()
    
    # Spin the node so the callback function is called.
        rclpy.spin(image_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
        image_publisher.destroy_node()
    
    # Shutdown the ROS client library for Python
        rclpy.shutdown()
    
if __name__ == '__main__':
    main()
