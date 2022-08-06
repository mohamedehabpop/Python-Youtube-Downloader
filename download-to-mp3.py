# dowmloads any video on youtube to mp3 file 
import pafy 

# you should add the video link here 
video = pafy.new('add the link of the video here ')

audiostream = video.getbestaudio()

audiostream.download()
