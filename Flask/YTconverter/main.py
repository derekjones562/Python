import os

from converter import Converter
from flask import Flask, render_template, redirect, url_for, request

from pytube import YouTube


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('yt_converter.html', **request.args)


@app.route('/extract_mp3/', methods=['POST'])
def extract_mp3():
    r = request
    data = r.form
    url = data['url']
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download('./mp4/')
    c = Converter(ffmpeg_path='/usr/local/bin/ffmpeg', ffprobe_path='/usr/local/bin/ffprobe')
    options = {
        'format': 'mp3',
        'audio': {
            'codec': 'mp3',
            'bitrate': '22050',
            'channels': 1
        }
    }
    infile_name = './mp4/' + stream.default_filename
    outfile_name = './mp3/'+ stream.default_filename.replace(".mp4", ".mp3")
    conv = c.convert(infile_name, outfile_name, options)
    for timecode in conv:
        pass
    os.remove(infile_name)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
