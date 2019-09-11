#Gujarati Text 

from gtts import gTTS

text="Tu job nathi kartho. Nawro cho. Nawro Chokro. Detko jem cho."
speech=gTTS(text,'gu')

speech.save("audio3.mp3 ")
