from flask import Flask, render_template, request
import socket
import pyautogui
import logging
import random

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

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
    return render_template('index.html', ip=ip, name=NAME)


@app.route("/incVolume")
@app.route("/decVolume")
def changeVolume():
    command = request.path
    if("inc" in command):
        pyautogui.press("volumeup")
    else:
        pyautogui.press("volumedown")
    return "-- Nothing --"


@app.route("/seekLeft")
@app.route("/seekRight")
def Seek():
    command = request.path
    if("Right" in command):
        pyautogui.press("right")
    else:
        pyautogui.press("left")
    return "-- Nothing --"


@app.route("/Space")
def Space():
    command = request.path
    if("space" in command):
        pyautogui.press("space")
    return "-- Nothing --"


@app.route("/Enter")
def Enter():
    command = request.path
    if("Enter" in command):
        pyautogui.press("enter")
    return "-- Nothing --"


@app.route("/CtrlF4")
def CtrlF4():
    command = request.path
    if("Ctrl" in command):
        pyautogui.hotkey("ctrl", "f4")
    return "-- Nothing --"


if __name__ == '__main__':
    print('--------------------------------------------------')
    print('--------------------------------------------------')
    print("Your Reference Number: " + str(REFERENCE))
    print('Access host at:' + get_ip()+':5000/'+str(REFERENCE))
    print('--------------------------------------------------')
    print('--------------------------------------------------')
    print()
    app.run(host="0.0.0.0")
