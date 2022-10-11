import gtts
from mutagen.mp3 import MP3

def audio_generation(text,path):
    print(text)
    audio_path = path + "audioVideo\\"
    tts = gtts.gTTS(text,slow=True)
    tts.save(audio_path + "audio.mp3")



def audio_length(path):
    audio_path = path + "audioVideo\\audio.mp3"
    try:
        audio = MP3(audio_path)
        length = audio.info.length
        return length
    except:
        return None