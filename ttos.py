# pip install gtts playsound

from gtts import gTTS
from playsound import playsound 

tts = gTTS("Hi guys finish your code. NOW!")
tts.save("speech.mp3")
print("hey")

playsound('speech.mp3')

