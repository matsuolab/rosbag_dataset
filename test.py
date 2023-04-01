import yaml

topics_path = 'config/topics_to_save.yml'
with open(topics_path, "r") as f:
    topics = yaml.load(f, Loader=yaml.FullLoader)
    if (topics == None):
        topics = "-a"
    print('rosbag record ' + topics)

print(topics)