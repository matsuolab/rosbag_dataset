# rosbag_dataset

## Overview

This is a node that handles the start and stop of rosbag.
The bag file is saved in `~/dataset/`.

## usage
```
$ mkdir ~/dataset
$ mkdir -p catkin_ws/src && cd catkin_ws/src
$ git clone https://github.com/matsuolab/teleop_ros.git
$ cd .. && catkin build
$ source devel/setup.bash
$ roslaunch rosbag_dataset rosbag_dataset.launch

