from moviepy.editor import *
import os
import glob


def generate_and_merge_audio_video(noun_list,path,length):
    video_path = path + "audioVideo\\"
    audio_path = path + "audioVideo\\audio.mp3"
    image_path = path + "images\\"
    # video_download_path = path + "audioVideo\\"
    image_list=[]
    for i in noun_list:
        
        a = i + ".png"
        print(a)    
        image_list.append(a)
    print(image_list)


    images=[]
    for i in image_list:
        images.append(image_path+i)
    print(images)
    k = length/len(image_list)
    print(k)
    clips = [ImageClip(m).set_duration(k)
        for m in images]

    concat_clip = concatenate_videoclips(clips, method="compose")
    video = concat_clip.write_videofile(video_path + "video.mp4", fps=24)

    videoclip = VideoFileClip(video_path+"video.mp4")
    audioclip = AudioFileClip(audio_path)

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(video_path + "output_video.mp4")


