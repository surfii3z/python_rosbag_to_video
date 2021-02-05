'''
Rename

root_directory
    - sub_directory_1
        - 000080.png
        - 000081.png
        - 000082.png
        - ...
    - sub_directory_2
        - 000100.png
        - 000101.png
        - ...
    - ...

to

root_directory
    - sub_directory_1
        - 000000.png
        - 000001.png
        - 000002.png
        - ...
    - sub_directory_2
        - 000000.png
        - 000001.png
        - 000002.png
        - ...
    - ...
'''
import glob
import os


ROOT_PATH="/home/jedsadakorn/git/python_rosbag_to_video/output/workbench_with_boxes/"
list_of_directory = glob.glob(ROOT_PATH + "part*")
list_of_directory = sorted(list_of_directory)

for idx_folder, folder_path in enumerate(list_of_directory):
    list_of_files = glob.glob(folder_path + "/*.png")
    list_of_files = sorted(list_of_files)
    for idx, path in enumerate(list_of_files):
        directory = path[:-10]
        os.rename(path, directory + "{:06d}.png".format(idx))

