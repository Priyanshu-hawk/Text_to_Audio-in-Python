#text to audio
from gtts import gTTS
from playsound import playsound

print("You can Listen to audio in 'audio' folder!!")
print("But it will replace by new audio, when you run this program next time!!\n")
audio = "audio/audio"
language = "en"
l_P = "y"
addon = 0
while l_P.lower() == "y":
    addon = addon + 1
    conv = str(addon)
    extension = ".mp3"
    fileA = audio + conv + extension
    test = str(input("Enter the text: "))
    if test.lower() == "out":
        break
    sp = gTTS(text = test, lang = language,slow=False)
    sp.save(fileA)
    playsound(fileA)
    


    
