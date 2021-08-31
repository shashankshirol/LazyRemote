# LazyRemote

Picture this, you are watching a series/movie on you PC and to enjoy the content better you switch from your uncomfortable chair to your bed only to realize the volume is too low or you missed a scene while munching on chips. This has happened to the best of us. But, fret not for now we have LazyRemote.

## Usage:

- Run the python script in the background. Open up the host webpage(address displayed on the terminal or scan QR) on your phone and Voila, all the necessary media controls on your PHONE!!!
- But, what if other people open the host webpage and start tinkering with your controls? Don't worry! LazyRemote has you covered, when accessing your host webpage, enter the REFERENCE number that is generated randomly every session. So, no one can control your PC except for YOU!
- Take a look at the images below to get a better idea!

**NOTE: Make sure both your phone and your PC are on the same network.**

## Requirements:

- `python 3.6+` available at: https://www.python.org/downloads/
- And, everything in the `requirements.txt` file. Run: `pip install -r requirements.txt`
- MOST IMPORTANTLY, this has only been tested on Windows. Don't know if it'll work on Linux/MacOS.
- FINALLY, to be a lazy bum.

## Images:

### Terminal:

<img src="https://github.com/shashankshirol/LazyRemote/blob/main/Images/LazyRemoteTerminal.png" width="768">

### Your Phone:

<img src="https://github.com/shashankshirol/LazyRemote/blob/main/Images/LazyRemotePhone.png" width="256">

## Installation and Running:

- Install Python from: (Download the latest version AND make sure you check 'Add Python to PATH checkbox while installing') https://www.python.org/downloads/
- Download this repo as a zip (click on the green button that says 'Code' above) and extract to any suitable location.
- Open a command prompt inside the folder `LazyRemote-main` (Where you extracted the zip contents). 
  Note: You can `cd` to the said folder in any command prompt window or type in `cmd` in the location specifier up top once you're in the folder.
- Run `pip install -r requirements.txt` on the command prompt window to install all the dependencies.
- With everything set up, run `python app.py` to launch the program and access the host (refer the pictures) with your mobile device (now, your LazyRemote)
- Leave the program running in the background while you stream your content.
- Once you want to stop, click on the command prompt window you left running and press `CTRL + C`
- Next time you want to use the service, open up a command prompt window in the said folder like before, and run `python app.py` and follow the on-screen instructions.
- Embrace being Lazy

**NOTE: Make sure both your phone and your PC are on the same network.**

### Bonus:

Add the folder to your PATH variable, instruction: [Running Python Scripts from anywhere under Windows](https://correlated.kayako.com/article/40-running-python-scripts-from-anywhere-under-windows)

After doing this, you'll be able to run the script from any command prompt window, just type `app.py`

## Use-cases:

Apart from having to change volume and seeking to a missed part, LazyRemote can also:

- Pause/Play content using the SPACE key
- Allow seeking to a particular point using the ENTER key (Useful on Netflix)
- And, if you are feeling frisky and watching something you shouldn't (We don't judge, promise), LazyRemote can also trigger a hotkey (CTRL+F4) to close the current tab (works on Chrome)
