#!python3
from flask import Flask, render_template, redirect, url_for, request

from pytube import YouTube
#from flask_socketio import SocketIO
app = Flask(__name__)
#socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('yt_converter.html', **request.args)


@app.route('/download_mp4/', methods=['POST'])
def download_mp4():
    r = request
    data = r.form
    url = data['url']
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).filter(file_extension='mp4').first()
    stream.download('./mp4/')
    return redirect(url_for('index'))


# if __name__ == "__main__":
#     app.run(debug=False)
