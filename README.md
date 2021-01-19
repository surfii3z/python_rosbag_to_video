# python_rosbag_to_video

This repo is the python script to extract video from rosbag

# Quick Start
1) change `BAG_PATH` in [extract.py](https://github.com/surfii3z/python_rosbag_to_video/blob/ef016e24073f25b9c12b6f0d4fca59eb34891b1b/extract.py#L12) to the rosbag file path
2) change `OUTPUT_PATH` in [extract.py](https://github.com/surfii3z/python_rosbag_to_video/blob/ef016e24073f25b9c12b6f0d4fca59eb34891b1b/extract.py#L13) to the output path for images

``` bash
# run this to extract images from rosbag
python extract.py

# images to videos
# might need to install ffmpeg
ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4
```
