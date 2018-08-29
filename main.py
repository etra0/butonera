from flask import Flask, render_template, jsonify
import os
import subprocess
import tbot
import netifaces as ni

app = Flask(__name__)


@app.route("/")
def index():
    files = get_sounds()
    return render_template("index.html", files=files)


def get_sounds():
    extensions = ('mp3', 'wav', 'ogg')
    files = [f for f in os.listdir("./static/sounds/") if f.endswith(extensions)]
    return sorted(files)


@app.route("/get_sounds/")
def api_get_sounds():
    files = get_sounds()
    return jsonify(files)


@app.route("/play_sound/<filename>")
def play_sound(filename):
    command = "mpv {}".format("static/sounds/" + filename)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return filename


if __name__ == '__main__':
    ifs = sorted([x for x in ni.interfaces() if x.startswith(('enp', 'wlp'))])
    addresses = [
        ni.ifaddresses(x)[ni.AF_INET][0]['addr']
        for x in ifs if ni.AF_INET in ni.ifaddresses(x).keys()
    ]
    tbot.run_tbot(addresses[0])
    app.run(host=addresses[0])