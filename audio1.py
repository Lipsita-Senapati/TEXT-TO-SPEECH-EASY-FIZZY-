#import library
from gtts import gTTS
text="HELLO Everyone! Python is fun to Learn. Today I explored the library which helps to convert text into speech. Isn't it great?"
#By default language is english
speech=gTTS(text)
#Saving the audio file
speech.save("audio1.mp3 ")
