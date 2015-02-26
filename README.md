# Bing Wallpapaer for Mac
A simple Python script to download Bing image of the day and set it as wallpaper on your Mac OS X.

## About
Ever since the switch to Mac, I've kinda been missing [PyBingWallpaper](https://github.com/genzj/pybingwallpaper). So I wrote this script to do pretty much the same thing. Microsoft provides JSON API to get the images. This makes things so much easier compared to my initial idea, which was to scrape the webpage. 

PS: This is only a Python script. You can convert it to an app with something likee `py2app` if you want. What you do with it is entirely up to you. I'll probably make a native OS X app for this since I've been learning Swift lately.

## Usage
You can modify the Configurations section to set your own image directory and country code. Wallpapers will be saved to `/Users/USERNAME/Pictures/BingWallpaper` by default.

[Requests](http://docs.python-requests.org/en/latest/) was used to simplfy the process. Make sure you have it installed before running the script.

## License
Who cares... Do whatever you want with it.