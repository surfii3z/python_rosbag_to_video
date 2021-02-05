# ref: https://programmersought.com/article/21404945818/
# images to videos: ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4

import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

BAG_PATH = '/home/jedsadakorn/Desktop/bag_2/workbench_boxes_low_alt_2.bag'
OUTPUT_PATH = '/home/jedsadakorn/git/python_rosbag_to_video/output/workbench_boxes_low_alt_2/'
SAMPLE_FREQ = 2

class ImageFromBag():

    def __init__(self, bag_path, output_path):
        self.bridge = CvBridge()

        with rosbag.Bag(bag_path) as bag:
            image_counter = 0
            for idx , (topic, msg, t) in enumerate(bag.read_messages(topics=['/camera/color/image_raw'])):
                try:
                    if idx % SAMPLE_FREQ == 0:
                        cv_image = self.bridge.imgmsg_to_cv2(msg)
                        image_name = '{:06d}.png'.format(image_counter)
                        cv2.imwrite(output_path + image_name, cv_image)
                        print("Write image: {}".format(image_name))
                        image_counter += 1
                except CvBridgeError as e:
                    print(e)
                

if __name__ == '__main__':
    try:
        image_from_bag = ImageFromBag(BAG_PATH, OUTPUT_PATH)
    except rospy.ROSInterruptException:
        pass
