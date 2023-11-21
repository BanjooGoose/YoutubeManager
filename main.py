from ymDef import getAudio, getVideo, getPlaylist


def main():
    while True:
        print('=======YOUTUBE_MANAGER=========')
        print('1. Скачать видео\n2. Скачать только аудио\n3. Скачать плейлист\n4. Выйти')
        print('===============================')
        a = input()
        if a == '1':
            getVideo()
        elif a == '2':
            getAudio()
        elif a == '3':
            getPlaylist()
        elif a == '4':
            break

if __name__ == '__main__':
    main()