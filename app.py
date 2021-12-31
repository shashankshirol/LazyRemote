from flask import Flask, render_template, request, redirect, url_for
import socket
import pyautogui
import logging
import random
import qrcode
import PIL

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
pyautogui.FAILSAFE = False

NAME = socket.gethostname()
REFERENCE = random.randint(1111,9999)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = str(s.getsockname()[0])
    s.close()
    return ip

@app.route("/"+str(REFERENCE))
def home():
    ip = get_ip()
    return render_template('index.html', ip=ip, name=NAME, reference=REFERENCE)


@app.route("/"+str(REFERENCE)+"/incVolume")
@app.route("/"+str(REFERENCE)+"/decVolume")
@app.route("/"+str(REFERENCE)+"/Mute")
def changeVolume():
    command = request.path
    if("inc" in command):
        pyautogui.press("volumeup")
    elif("dec" in command):
        pyautogui.press("volumedown")
    else:
        pyautogui.press("volumemute")
    
    return ""


@app.route("/"+str(REFERENCE)+"/seekLeft")
@app.route("/"+str(REFERENCE)+"/seekRight")
def Seek():
    command = request.path
    if("Right" in command):
        pyautogui.press("right")
    else:
        pyautogui.press("left")

    return ""


@app.route("/"+str(REFERENCE)+"/PlayPause")
def PlayPause():
    command = request.path
    if("PlayPause" in command):
        pyautogui.press("space")
    
    return ""


@app.route("/"+str(REFERENCE)+"/Enter")
def Enter():
    command = request.path
    if("Enter" in command):
        pyautogui.press("enter")

    return ""


@app.route("/"+str(REFERENCE)+"/Mouse")
def Mouse():
    return render_template('ham_mouse.html', name=NAME, reference=REFERENCE)


@app.route("/"+str(REFERENCE)+"/Mouse/action")
def MouseAction():
    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', 0, type=int)
    pyautogui.moveRel(x, y)
    if ( x == 0 and y == 0):
        pyautogui.click()

    return ""


@app.route("/"+str(REFERENCE)+"/CtrlF4")
def CtrlF4():
    command = request.path
    if("Ctrl" in command):
        pyautogui.hotkey("ctrl", "f4")
    return ""


if __name__ == '__main__':
    host = get_ip()+':5000/'+str(REFERENCE)
    print('--------------------------------------------------')
    print('--------------------------------------------------')
    print("Your Reference Number: " + str(REFERENCE))
    print('Access host at:' + host)
    print('Or, scan the QR code shown!')
    print('--------------------------------------------------')
    print('Press Ctrl+C to Stop')
    print('--------------------------------------------------')
    print()
    img = qrcode.make(host)
    img.show()
    app.run(host="0.0.0.0")
