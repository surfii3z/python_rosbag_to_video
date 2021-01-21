# python_rosbag_to_video

This repo is the python script to extract video from rosbag

Work right away with `python2`.

It does NOT work with `python3` for now because of cv_bridge.

# Dependencies
Install the following package using pip
```bash
# Cryptodome
pip install pycryptodomex
# gnupg
pip install gnupg
```

# Quick Start
1) change `BAG_PATH` in [extract.py](https://github.com/surfii3z/python_rosbag_to_video/blob/ef016e24073f25b9c12b6f0d4fca59eb34891b1b/extract.py#L12) to the rosbag file path
2) change `OUTPUT_PATH` in [extract.py](https://github.com/surfii3z/python_rosbag_to_video/blob/ef016e24073f25b9c12b6f0d4fca59eb34891b1b/extract.py#L13) to the output path for images
3) change the topic name for rgb sequences in [extract.py](https://github.com/surfii3z/python_rosbag_to_video/blob/4c1a43e44918d7f48c3a0c7f66caf91f757bc016/extract.py#L21)

``` bash
# run this to extract images from rosbag
python extract.py

# images to videos
# might need to install ffmpeg
ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4
```

