from flask import Flask, render_template, jsonify
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
    app.run(host="192.168.0.14")