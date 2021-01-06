#!/usr/bin/env python3

import rospy
import rospkg
import datetime
import os
import yaml
import time
from threading import Thread
from std_msgs.msg import Bool, Int8


class LoggerCommand:
    STOP = 0
    START = 1
    ERROR = 2


class ROSBagHandler():
    def __init__(self):
        self.logging = False
        os.system('rostopic list')

        # self.thread = Thread(target=self.threaded_rosbag)

        rospack = rospkg.RosPack()
        package_path = rospack.get_path('rosbag_dataset')

        topics_path = package_path + '/config/topics_to_save.yml'
        with open(topics_path, "r") as f:
            self.topics = yaml.load(f, Loader=yaml.FullLoader)
            if (self.topics == None):
                self.topics = "-a"
            print('rosbag record ' + self.topics)

        self.dataset_name = rospy.get_param('dataset_name', '')
        self.thread = Thread(target=self.threaded_rosbag)
        self.dataset_path = os.path.expanduser("~") + '/dataset/'
        if self.dataset_name:
            # self.dataset_path = os.path.join(self.dataset_path, self.dataset_name)
            self.dataset_path = self.dataset_path + self.dataset_name + "/"
            if not os.path.isdir(self.dataset_path):
                print("mkdir done")
                os.makedirs(self.dataset_path)

        rospy.Subscriber('/logging', Int8, self.command_cb)
        # rospy.Service('logging_service', Trigger, self.logging_cb)
        rospy.spin()

    def threaded_rosbag(self):
        now = datetime.datetime.now()
        self.bagfile = now.strftime('%Y%m%d_%H%M%S_%f') + ".bag"
        os.system('rosbag record ' + self.topics + ' -O ' + self.dataset_path + self.bagfile + ' __name:=rosbag_node')

    def command_cb(self, msg):
        if msg.data == LoggerCommand.START and self.logging == False:
            self.logging = True
            thread = Thread(target=self.threaded_rosbag)
            thread.start()

        elif msg.data == LoggerCommand.STOP and self.logging == True:
            self.logging = False
            os.system('rosnode kill /rosbag_node')

        elif msg.data == LoggerCommand.ERROR and self.logging == True:
            self.logging = False
            os.system('rosnode kill /rosbag_node')
            for j in range(60):
                time.sleep(1)
                if os.path.exists(self.dataset_path + self.bagfile):
                    os.remove(self.dataset_path + self.bagfile)
                    print("delete succeeded")
                    break
                else:
                    if j == 60:
                        print("!!!!!!! rosbag delete timeout !!!!!!!!!!!")
                    else:
                        print("wait a moment")
                        continue

        else:
            print("receive " + msg.data + " but already /logging is " + str(self.logging))


def main():
    rospy.init_node('rosbag_handler')
    ROSBagHandler()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
