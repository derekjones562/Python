#!python

import os

from converter import Converter


def main():
    print("starting conversions")
    mp4Dir = './mp4/'
    mp3Dir = './.mp3/'
    filenames = getFilenames(mp4Dir)
    c = Converter(ffmpeg_path='/usr/bin/ffmpeg', ffprobe_path='/usr/bin/ffprobe')
    options = {
        'format': 'mp3',
        'audio': {
            'codec': 'mp3',
            'bitrate': '22050',
            'channels': 1
        }
    }

    try:
        os.makedirs(mp3Dir)
    except FileExistsError:
        # directory already exists
        pass

    for infile_name in filenames:
        outfile_name = mp3Dir + infile_name.replace(".mp4", ".mp3")
        conv = c.convert(mp4Dir+infile_name, outfile_name, options, None)
        for timecode in conv:
            print("Converting (%f) ....\r" % timecode)
        os.remove(mp4Dir+infile_name)


def getFilenames(path):
    files = []
    for x in os.listdir(path):
        if x.endswith(".mp4"):
            files.append(x)
    return files


if __name__ == "__main__":
    main()
