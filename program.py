# YouTube downloader
from pytube import YouTube
from wget import download
print('YouTube downloader | Creator - artur-asimov\n')

link = input('Paste your video link here: ')
yt = YouTube(link)

print(f'\nVideo title is - {yt.title}')

yn = input('Are you sure you want to download this video? (y/n): ')

if yn == 'y' or yn == 'Y' :
    print('\nDownloading video ...')
    video = yt.streams.get_highest_resolution()
    video.download(f'./{yt.title}')

    thumbnail = yt.thumbnail_url;
    print('Downloading thumbnail ...')
    download(thumbnail, out=f'./{yt.title}', bar=None)

    print('\nOkay, it\'s done!')
else :
    print('\nOkay, bye!')