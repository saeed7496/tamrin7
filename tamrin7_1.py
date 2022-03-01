
from moviepy import editor

video=editor.VideoFileClip('tatal.mp4')
video.audio.write_audiofile('tatal.mp3')



