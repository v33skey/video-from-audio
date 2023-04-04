import moviepy.editor
from pathlib import Path

name = input('Enter video name: ')
video_file = Path(name)

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio

audio.write_audiofile(f'{video_file.stem}.mp3')

