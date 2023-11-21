from pytube import YouTube
from pytube import Playlist


def getData():
    print("Enter URL: ")
    link = input()
    print('--------')
    return link

def getStream():
    link = getData()
    yt = YouTube(link)
    print("Title: ", yt.title)
    return yt
    

def getAudio():
    yd = getStream().streams.get_audio_only()
    yd.download('C:/Syncthing/PhoneLib/Podcasts')
    print("Success!!")

def getVideo():
    yd = getStream().streams.get_by_resolution('360p')
    yd.download('C:/Syncthing/PhoneLib/Video')
    print("Success!!")

def getPlaylist():
    yp = Playlist(getData())
    print('Title: ', yp.title)
    counter = 0
    for video in yp.videos:
        counter += 1
        video = video.streams.get_by_resolution('360p')
        print(f'{counter} {video.title}')
        video.download(f'C:/Syncthing/PhoneLib/Video/{yp.title}', filename_prefix=f'{counter} ')
    print("Success!!")