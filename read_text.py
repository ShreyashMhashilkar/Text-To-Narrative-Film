from download_images import convert_images
from generate_audio import audio_generation
from generate_video import generate_and_merge_audio_video
from generate_audio import audio_length
from textblob import TextBlob
from download_images import download_img
import glob
import time
def readText(text,path):
    audio_generation(str(text),path)   
    print(text)
    textsplit = text.split(".")
    print(textsplit)
    noun_list = []
    for line_text in textsplit:
        print(line_text)
        blob = TextBlob(line_text)
        for noun in blob.noun_phrases:
            print(noun,"printing noun")
            noun_list.append(noun)
    print(noun_list)
    download_img(noun_list)
    convert_images()       
    length = audio_length(path)
    print(length)
    generate_and_merge_audio_video(noun_list,path,length)
    files = glob.glob(path + "audioVideo\\*")

    data=[]
    for f in files:
        if "output_video.mp4" in f:
            data.append(True)
        else:
            data.append(False)

    if True in data:
        return True
    else:
        return False
    





