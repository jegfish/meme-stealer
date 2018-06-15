# meme-stealer
Generates meme slideshows with text-to-speech narration.

[Example video output.](https://youtu.be/NLQYBwTV7dM)

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