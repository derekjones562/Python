#!python3
import time

from flask import Flask, render_template, redirect, url_for, request, send_file, Response

import yt_dlp
import logging

from filenamePostProcessor import FilenameCollectorPP

logger = logging.getLogger(__name__)

# from flask_socketio import SocketIO
app = Flask(__name__)
# socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('yt_converter.html', **request.args)


@app.route('/download_mp4/', methods=['GET'])
def redirect_after_download():
    return redirect("/")


@app.route('/download_mp4/', methods=['POST'])
def download_mp4():
    def generate():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(filename_collector)
            error_code = ydl.download(url)
            if error_code:
                logger.warning("ErrorCode: " + error_code)
                return redirect(url_for('index'))
            with open(filename_collector.filenames[0], "rb") as song_dong:
                dong_data = song_dong.read(1024)
                while dong_data:
                    yield dong_data
                    dong_data = song_dong.read(1024)

    r = request
    data = r.form
    url = data['url']
    filename_collector = FilenameCollectorPP()
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            }],
        'outtmpl': {'default': './mp4/%(title)s [%(id)s].%(ext)s'},
    }
    filename = getfilenamefromurl(url)
    return Response(generate(), mimetype="audio/mp3", headers={'Content-Disposition': 'attachment; filename = "' + filename + '"'})

    # return redirect(url_for('index'))


def getfilenamefromurl(url):
    opts = {
        'outtmpl': {'default': '%(title)s [%(id)s]'}
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(ydl.sanitize_info(info)) + '.mp3'
        return filename


# if __name__ == "__main__":
#     app.run(debug=False)
