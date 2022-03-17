# meme-stealer
Generates video slideshows of memes.

Downloads recent meme images using the Reddit API, fits images onto a solid color background, uses Optical Character Recognition (OCR) to recognize text in the images, generates text-to-speech-audio, and finally generates a video slideshow with each meme showing for a minimum time or for the length of the audio.

## Installing
Make sure you have `git`, `python3`, and `pipenv`.
```sh
git clone https://github.com/Altarrel/meme-stealer.git
cd meme-stealer

# Setup pipenv
pipenv --three
pipenv install
```

## Usage
```sh
pipenv run python main.py -l 50

# Without specifying meme limit (defaults to 25)
pipenv run python main.py
```

The video output will be saved to `videos` folder as a `.mp4` with the filename being the date in the format `YYYY-MM-DD`.
