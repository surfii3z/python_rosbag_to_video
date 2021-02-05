import glob
import os

ROOT_PATH="/home/jedsadakorn/git/python_rosbag_to_video/output/"
NAME = "workbench_boxes_low_alt_2"
list_of_directory = glob.glob(ROOT_PATH + NAME + "/part*")
list_of_directory = sorted(list_of_directory)

for idx_folder, folder_path in enumerate(list_of_directory):
    sub_directory_name = folder_path.split('/')[-1]
    list_of_files = glob.glob(folder_path + "/*.png")
    list_of_files = sorted(list_of_files)
    text_file_name = NAME + "_" + sub_directory_name
    with open(ROOT_PATH + NAME + "/" + "{}.txt".format(text_file_name), 'w') as f:
            for idx, path in enumerate(list_of_files):
                tokens = path.split("/")
                f.write(tokens[-2] + "/" + tokens[-1] + "\n")

    f.close()


