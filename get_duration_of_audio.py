from mutagen.mp3 import MP3

def audio_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None

audio_path = r"C:\Users\lenovo\Documents\TextToNarrativeFilms\hello.mp3"
length = mutagen_length(audio_path)
print("duration sec: " + str(length))
print("duration min: " + str(int(length/60)) + ':' + str(int(length%60)))