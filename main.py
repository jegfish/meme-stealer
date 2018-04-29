import datetime
import subprocess

from get_memes import get_memes
from slideshow import make_slideshow

# Get date string to be used for folder name
date = datetime.datetime.now().strftime("%Y-%m-%d")

image_paths = get_memes(date)
video_path = make_slideshow(image_paths, date)
print(video_path)
output = subprocess.check_output(["python",
                "youtube-upload/bin/youtube-upload",

                "--title",
                date,

                "--client-secrets",
                "client_secrets.json",

                "--playlist",
                "/r/dankmemes",

                video_path
])

video_id = output.strip()
print("https://www.youtube.com/watch?v=" + video_id)