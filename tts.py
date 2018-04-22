import os

# Import the required module for text 
# to speech conversion
from gtts import gTTS

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
def text_to_speech(text, filename):
    myobj = gTTS(text=text, lang="en", slow=False)
    # save to file
    myobj.save(filename)