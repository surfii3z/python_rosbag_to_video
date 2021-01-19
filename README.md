# python_rosbag_to_video

# Quick Start
1) change `BAG_PATH` in extract.py to the rosbag file path
2) change `OUTPUT_PATH` in extract.py to the output path for images

``` bash
# run this to extract images from rosbag
python extract.py

# images to videos
# might need to install ffmpeg
ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4
```
