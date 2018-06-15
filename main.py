import datetime
import argparse

from get_memes import get_memes
from slideshow import make_slideshow

parser = argparse.ArgumentParser(description="Download memes from r/dankmemes "
                                             "and create a slideshow video with "
                                             "text to speech.")
parser.add_argument("-l", "--limit", const="25", nargs="?",
                    help="number of memes to include")
args = parser.parse_args()

# Get date string to be used for folder name
date = datetime.datetime.now().strftime("%Y-%m-%d")

image_paths = get_memes(date, args.limit)
video_path = make_slideshow(image_paths, date)
print(video_path)