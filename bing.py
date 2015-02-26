#!/usr/bin/env python

# Configurations

# Location to save downloaded wallpapers
# Leave the IMAGE_DIR empty to use default directory /Users/USERNAME/Pictures/BingWallpaper
# Or you can set your own custom directory
IMAGE_DIR = ''
# ISO country code
# eg. 'en-US', 'en-NZ', 'zh-CN' or just leave it
COUNTRY_CODE = ''


import requests, urllib
from os.path import join, expanduser, isfile, exists
from os import makedirs


# Apple Script to set wallpaper
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""


def get_wallpaper_path(file_name):
    if '' != IMAGE_DIR.strip():
        dir = IMAGE_DIR
    else:
        dir = join(expanduser("~"), 'Pictures/BingWallpaper1')

    if not exists(dir):
        makedirs(dir)

    file_path = join(dir, file_name)
    return file_path


# Download the image with given URL
def download_image(url):
    file_name = url.split('/')[-1]
    file_path = get_wallpaper_path(file_name)

    if isfile(file_path):
        print('Skipped - Image exists.')
    else:
        urllib.urlretrieve(url, file_path)
        print('Image downloaded --> ' + file_path)

    set_wallpaper(file_path)


# Set Finder wallpaper
# See http://stackoverflow.com/questions/431205/how-can-i-programatically-change-the-background-in-mac-os-x
def set_wallpaper(file_path):
    if isfile(file_path):
        import subprocess
        subprocess.Popen(SCRIPT%file_path, shell=True)
        print('Wallpaper set to ' + file_path)


def main():
    # See http://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
    
    # URL to return 8 images
    # url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8'
    # URL to return the newest image
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

    # Use country code if provided
    if '' != COUNTRY_CODE.strip():
        url += '&mkt=' + COUNTRY_CODE

    # Make the request
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json() # Get JSON
        images = json['images']

        # Multiple wallpapers
        # for i in range(len(images)):
        #     url = 'http://www.bing.com' + images[i]['url']
        #     download_image(url)

        # Only the newest one
        url = 'http://www.bing.com' + images[0]['url']
        download_image(url)
    else:
        print('Oops, something went wrong...')


if __name__ == '__main__':
    main()
