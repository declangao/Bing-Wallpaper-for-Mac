# Bing Wallpapaer for Mac
A simple Python script capable of batch-downloading and setting Bing picture of the day as wallpaper on your Mac OS X.

## About
Ever since the switch to Mac, I've kinda been missing [PyBingWallpaper](https://github.com/genzj/pybingwallpaper). So I wrote this script to do pretty much the same thing. 

Microsoft provides an API to get the images. This makes things so much easier compared to my initial idea, which was to scrape the webpage. 

PS: This is only a Python script. What you do with it is entirely up to you. I'll probably make a native OS X app for this since I've been learning Swift lately. Meanwhile, you can use **Automator** with `python PATH/bing.py` shell command to create an app that calls this script and configure it to run everytime you login. Click [here](http://stackoverflow.com/questions/6442364/running-script-upon-login-mac) for more details.

## Usage
You can modify the Configurations section to set your own image directory and country code. Wallpapers will be saved to **/Users/USERNAME/Pictures/BingWallpaper** by default.

Download today's Bing picture of the day and set it as wallpaper:

```
python bing.py
```

Use `-d` or `--download` argument to download and save the last 8 pictures without changing the current wallpaper. You might use this option if you want to change wallpapers automatically by adding the wallpaper directory in **System Preferences**.

```
python bing.py -d
```

Use `-h` or `--help` to display help message.

## License
Copyright [DeclanGao](http://twitter.com/DeclanGao/) © 2015.
Licensed under the MIT License.