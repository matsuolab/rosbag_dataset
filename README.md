# rosbag_dataset

## Overview

This is a node that handles the start and stop of rosbag.


## Usage
```
$ mkdir ~/dataset
$ mkdir -p catkin_ws/src && cd catkin_ws/src
$ git clone https://github.com/matsuolab/teleop_ros.git
$ cd .. && catkin build
$ source devel/setup.bash
$ roslaunch rosbag_dataset rosbag_dataset.launch [dataset_name:=hoge]
```

The bag file is saved in `~/dataset/`.  
If you specify [dataset_name], then it will be saved in `~/dataset/[dataset_name]`.

