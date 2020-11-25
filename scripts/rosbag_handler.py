#!/usr/bin/env python3

import rospy
import rospkg
import datetime
import os
from threading import Thread
from std_msgs.msg import Bool

class ROSBagHandler():
    def __init__(self):
        self.logging = False
        os.system('rostopic list')

        self.thread = Thread(target=self.threaded_rosbag)

        rospack = rospkg.RosPack()
        package_path = rospack.get_path('teleop_ros')
        # self.dataset_path = package_path + '/dataset/'
        self.dataset_path = '~/dataset/'
        
        command_sub_ = rospy.Subscriber('/logging', Bool, self.command_cb)
        rospy.spin()

    def threaded_rosbag(self):
        now = datetime.datetime.now()
        bagfile = now.strftime('%Y%m%d_%H%M%S_%f') + ".bag"
        os.system('rosbag record -a -O ' + self.dataset_path + bagfile + ' __name:=rosbag_node')

    def command_cb(self, msg):
        if msg.data == True and self.logging == False:
            self.logging = True
            thread = Thread(target=self.threaded_rosbag)
            thread.start()
    
        elif msg.data == False and self.logging == True:
            self.logging = False
            os.system('rosnode kill /rosbag_node')

        else:
            print("already /logging is " + str(self.logging))

def main():
    rospy.init_node('rosbag_handler')
    ROSBagHandler()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass
