# ref: https://programmersought.com/article/21404945818/
# images to videos: ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4

import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

BAG_PATH = ''
OUTPUT_PATH = ''

class ImageFromBag():

    def __init__(self, bag_path, output_path):
        self.bridge = CvBridge()

        with rosbag.Bag(bag_path) as bag:
            for idx , (topic, msg, t) in enumerate(bag.read_messages(topics=['/camera/color/image_raw'])):
                try:
                    cv_image = self.bridge.imgmsg_to_cv2(msg)
                    image_name = 'frame_{:06d}.png'.format(idx)
                    cv2.imwrite(output_path + image_name, cv_image)
                    print("Write image: {}".format(image_name))
                except CvBridgeError as e:
                    print(e)
                

if __name__ == '__main__':
    try:
        image_from_bag = ImageFromBag(BAG_PATH, OUTPUT_PATH)
    except rospy.ROSInterruptException:
        pass
