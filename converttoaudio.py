# Import the required module for text 
# to speech conversion + I JUST CAN'T get it running here for the speetch function, it run on my local machinejust not on AWS
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

def convert(address):
     
    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 
    myaudio = gTTS(text=address, lang=language, slow=False) 
        
    # Saving the converted audio in a mp3 file named 
    # welcome 
    myaudio.save("address.mp3") 
   
       
    if os.name == "posix":
        # Playing the converted file on MCox
        os.system("afplay address.mp3") 
    elif os.name == "nt":
        os.system("address.mp3")
    else: 
        os.name("address.mp3")

