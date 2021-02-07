import moviepy.editor

video = moviepy.editor.VideoFileClip("got a friend.mp4")
audio=video.audio 
audio.write_audiofile('got a friend.mp3')
