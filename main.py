from ymDef import getAudio, getVideo, getPlaylist


def main():
    while True:
        print('=======YOUTUBE_MANAGER=========')
        print('1. Download video\n2. Download audio only\n3. Download playlist\n4. Exit')
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