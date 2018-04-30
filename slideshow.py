import os

import cv2
from moviepy.editor import *
from moviepy.audio import *
import numpy

from img_to_text import img_to_text
from tts import text_to_speech

supported_formats = (".png", ".jpg", ".jpeg")
#Load image path of all images        
def load_img_paths(pathFolder):
    #empty list
    _path_image_list = []
    #Loop for every file in folder path
    for filename in os.listdir(pathFolder):
        #Image Read Path
        _path_image_read = os.path.join(pathFolder, filename)
        #Check if file path has supported image format and then only append to list
        if _path_image_read.lower().endswith(supported_formats):
            _path_image_list.append(_path_image_read)
    #Return image path list
    return _path_image_list

def ensure_even(image):
    h, w = image.shape[:2]
    resize = False
    if h % 2 != 0:
        h -= 1
        resize = True
    if w % 2 != 0:
        w -= 1
        resize = True
    if resize:
        image = cv2.resize(image, (w, h), cv2.INTER_AREA)
    return image

def overlay_image(image, background):
    # Overlay the image onto the background

    # load the input image, then add an extra dimension to the
    # image (i.e., the alpha transparency)

    # Get image/overlay/watermark dimensions and make sure they are even
    iH, iW = image.shape[:2]

    background = ensure_even(background)
    h, w = background.shape[:2]

    # Image resizing
    if iH > h or iW > w:
        img_new_w = None
        img_new_h = None
        if iH > h:
            ratio = iH / h
            img_new_h = h
            img_new_w = int(w / ratio)
        elif iW > w:
            ratio = iW / w
            img_new_w = w
            img_new_h = int(h / ratio)
        image = cv2.resize(image, (img_new_w, img_new_h), cv2.INTER_AREA)

    image = ensure_even(image)
    iH, iW = image.shape[:2]

    start_row = int((h - iH) / 2)
    end_row = int(h - start_row)
    start_col = int((w - iW) / 2)
    end_col = int(w - start_col)
    # put the image in the center of the background
    output = background.copy()
    output[start_row:end_row, start_col:end_col] = image
    a, b = output.shape[:2]

    return output

def make_slideshow(image_path, date):
    #Load image paths    
    img_path_list = load_img_paths(image_path)

    video_background = cv2.imread("background.png")
    if video_background is None:
        print("Couldn't find background.png")
        exit()
    img_clips = []
    i = 0
    # Overlay all images onto background
    for img_path in img_path_list:
        # Load and then resize/overlay image onto background
        img = cv2.imread(img_path)
        if img is None:
            print("Problem with {}".format(img_path))
        # Flip color of image so it doesn't look weird
        img = img[:,:,::-1]
        img = overlay_image(img, video_background)

        # Make sure ./temp_audio exists, if not then create it
        if not os.path.exists("./temp_audio"):
            os.makedirs("./temp_audio")

        # Get text
        text = img_to_text(img)
        tts_path = os.path.join("temp_audio", "{}.mp3".format(i))
        tts = True
        try:
            text_to_speech(text, tts_path)
        except Exception as e:
            if "No text to speak" in str(e):
                tts = False

        # Find duration for image based on tts length
        duration = 4
        if tts:
            tts_audio = AudioFileClip(tts_path)
            duration = tts_audio.duration
            tts_audio = tts_audio.set_duration(duration)

        # Make video clip out of image
        clip = ImageClip(img, duration=duration)
        if tts:
            clip = clip.set_audio(tts_audio)
        else:
            make_frame = lambda t : 2*[0]
            blank_audio = AudioClip.AudioClip(make_frame=make_frame, duration=duration)
            clip = clip.set_audio(blank_audio)
        print("Finished with {}".format(img_path))
        img_clips.append(clip)

        i += 1

    # background_audio = AudioFileClip("Catmosphere - Candy-Coloured Sky.mp3")
    concat_clip = concatenate_videoclips(img_clips)
    # audio = CompositeAudioClip([concat_clip.audio, background_audio])
    # Add background music
    # concat_clip = concat_clip.set_audio(audio.set_duration(concat_clip.duration))

    if not os.path.exists("./videos"):
        os.makedirs("./videos")
    path = "./videos/{}.mp4".format(date)
    concat_clip.write_videofile(path, fps=24)
    # Clean temp_audio folder
    print("Clearing temp_audio")
    files = os.listdir("./temp_audio")
    for file_name in files:
        os.remove("./temp_audio/{}".format(file_name))
    return path
