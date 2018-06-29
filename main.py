from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    files = get_sounds()
    return render_template("index.html", files=files)


def get_sounds():
    extensions = ('mp3', 'wav', 'ogg')
    files = [f for f in os.listdir("./static/sounds/") if f.endswith(extensions)]
    return files


@app.route("/play_sound/<filename>")
def play_sound(filename):
    command = "mpv {}".format("static/sounds/" + filename)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return filename
