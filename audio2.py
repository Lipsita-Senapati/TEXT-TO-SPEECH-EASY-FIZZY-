#Hindi Text

from gtts import gTTS
text="Kaise ho motu? Mujhe tumhari bahut yaad arahi hei."
speech=gTTS(text,'hi')

speech.save("audio2.mp3 ")
