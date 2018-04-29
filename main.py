import datetime

from get_memes import get_memes
from slideshow import make_slideshow

# Get date string to be used for folder name
date = datetime.datetime.now().strftime("%Y-%m-%d")

image_paths = get_memes(date)
video_path = make_slideshow(image_paths, date)
print(video_path)