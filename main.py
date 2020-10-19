import numpy
import cv2
from PIL import Image, ImageDraw
import os
from moviepy.editor import *
from tqdm import tqdm


def get_frame_count(path):  # literally
    cap = cv2.VideoCapture(path)
    return cap.get(cv2.CAP_PROP_FRAME_COUNT)


def get_fps(path):  # literally
    cap = cv2.VideoCapture(path)
    return cap.get(cv2.CAP_PROP_FPS)


def get_ratio(path):  # literally
    cap = cv2.VideoCapture(path)
    return cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


def video2imgs(path, size):  # convert video to list of images
    img_list = []
    cap = cv2.VideoCapture(path)
    with tqdm(total=get_frame_count(path)) as pbar:  # add progress bar
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale
                image = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)
                img_list.append(image)
            else:
                break
            pbar.update(1)
    cap.release()
    return img_list


def img2char(img):
    str = ".,:;+*?%S#@"
    str = str[::-1]
    result = []
    percents = img / 255
    indexes = (percents * (len(str) - 1)).astype(numpy.int)
    height, width = img.shape
    for row in range(height):
        line = ""
        for col in range(width):
            index = indexes[row][col]
            line += str[index] + " "
        result.append(line)
    return result


def imgs2chars(imgs):
    result = []
    for img in imgs:
        result.append(img2char(img))
    return result


def char2picture(picture_chars, width, height):
    img_i = Image.new("RGB", (width, height), (255, 255, 255))
    draw_i = ImageDraw.Draw(img_i)
    s = ""
    for line in picture_chars:
        s += line + '\n'
    draw_i.multiline_text((0, 0), s, fill="#000000")
    return cv2.cvtColor(numpy.asarray(img_i), cv2.COLOR_RGB2BGR)


def char2video(frame_array, width, height, fps=24):
    # part of output_silent
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(os.path.abspath(".") + '\\silent.avi', fourcc, fps, (width, height))
    with tqdm(total=len(frame_array)) as pbar:  # add progress bar
        for frame in frame_array:
            video.write(char2picture(frame, width, height))
            pbar.update(1)
    video.release()


def output_silent(path, width, height):
    # Save the temporary video without BGM
    imgs = video2imgs(path, (width, height))  # convert video to lists of frames
    video_chars = imgs2chars(imgs)  # convert frames to chars respectively
    char2video(video_chars, 1100, 960, get_fps(path))


def output_includemusic(path):
    # Get and save the BGM
    video = VideoFileClip(path)
    audio = video.audio
    audio.write_audiofile('tmp_music.mp3')

    # Combine audio and video
    video = VideoFileClip("silent.avi")
    audio_clip = AudioFileClip('tmp_music.mp3')
    video = video.set_audio(audio_clip)
    video.write_videofile("output.mp4")

    # delet temporary files
    if os.path.exists("tmp_music.mp3"):
        os.remove("tmp_music.mp3")

    if os.path.exists("silent.avi"):
        os.remove("silent.avi")


if __name__ == "__main__":
    path = "video.flv"

    ratio = get_ratio(path)
    width, height = int(ratio * 60), 60

    output_silent(path, width, height)
    output_includemusic(path)
