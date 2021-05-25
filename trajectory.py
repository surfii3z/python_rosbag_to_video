# ref: https://programmersought.com/article/21404945818/
# images to videos: ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4

import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

BAG_PATH = '/home/jy/Downloads/test_tello_crop_exp.bag'
OUTPUT_PATH = '/home/jy/git/python_rosbag_to_video/'
SAMPLE_FREQ = 37

class TrajectoryFromBag():

    def __init__(self, bag_path, output_path):
        self.bridge = CvBridge()

        with open("optitrack.txt", "w") as f:
            with rosbag.Bag(bag_path) as bag:
                for idx , (topic, msg, t) in enumerate(bag.read_messages(topics=['/vrpn_client_node/Tello/pose'])):
                    if idx % SAMPLE_FREQ == 1:
                        x, y, z  = msg.pose.position.x, msg.pose.position.y, msg.pose.position.z
                        qx, qy, qz, qw = msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w
                        f.write("{} {} {} {} {} {} {} {}\n".format(idx, y, -z, x, qx, qy, qz, qw))
                print("Finish writing")
                
                

if __name__ == '__main__':
    try:
        trajectory_from_bag = TrajectoryFromBag(BAG_PATH, OUTPUT_PATH)
    except rospy.ROSInterruptException:
        pass
