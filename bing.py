#!/usr/bin/env python

# Configurations

# Location to save downloaded wallpapers
# Leave the IMAGE_DIR empty to use default directory /Users/USERNAME/Pictures/BingWallpaper
# Or you can set your own custom directory
IMAGE_DIR = ''
# ISO country code
# eg. 'en-US', 'en-NZ', 'zh-CN' or just leave it
COUNTRY_CODE = ''


import requests, urllib, sys
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
        dir = join(expanduser("~"), 'Pictures/BingWallpaper')

    if not exists(dir):
        makedirs(dir)

    file_path = join(dir, file_name)
    return file_path


# Download a image with given URL
def download_image(url, download_only=False):
    file_name = url.split('/')[-1]
    file_path = get_wallpaper_path(file_name)

    if isfile(file_path):
        print('Skipped - ' + file_name + ' exists already.')
    else:
        urllib.urlretrieve(url, file_path)
        print('Image downloaded --> ' + file_path)

    if not download_only:
        set_wallpaper(file_path)


# Set Finder wallpaper
# See http://stackoverflow.com/questions/431205/how-can-i-programatically-change-the-background-in-mac-os-x
def set_wallpaper(file_path):
    if isfile(file_path):
        import subprocess
        subprocess.Popen(SCRIPT%file_path, shell=True)
        print('Wallpaper set to ' + file_path)


# Display help message
def print_help_message():
    msg = '''
Bing Wallpaper for Mac version 1.1
By Declan Gao  http://declangao.me

Bing Wallpaper for Mac can batch download and set Bing image of the day as wallpaper on OS X.

Usage: 
python bing.py [option]

no argument         download today's picture of the day and set it as wallpaper
-d or --download    download and save the last 8 pictures withouth changing the current wallpaper
-h or --help        display this help message
    '''
    print(msg)
    sys.exit()


def main():
    # Check arguments
    if len(sys.argv) == 1:
        flag_download_only= False
    elif len(sys.argv) == 2:
        if '-d' == sys.argv[1] or '--download' == sys.argv[1]:
            flag_download_only = True
        elif '-h' == sys.argv[1] or '--help' == sys.argv[1]:
            print_help_message()
        else:
            print('Invalid argument!')
            print_help_message()
    else:
        print('Invalid arguments!')
        print_help_message()

    # Choose a proper URL
    # The API only returns 8 pictures at most. No need to set the number higher than 8.
    # See http://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
    if flag_download_only:
        url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8'
    else:
        # Set n=8 to get only the newest picture of the day
        url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

    # Use country code if provided
    if '' != COUNTRY_CODE.strip():
        url += '&mkt=' + COUNTRY_CODE

    # Make the request
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json() # Get JSON

        if 'images' in json:
            images = json['images']
        else:
            sys.exit('JSON error. Please try again later...')
        
        # Start downloading!
        print('Downloading...')
        for i in range(len(images)):
            url = 'http://www.bing.com' + images[i]['url']
            if flag_download_only:
                download_image(url, True)
            else:
                download_image(url)
    else:
        print('Cannot reach server. Please check your internet connection...')


if __name__ == '__main__':
    main()
