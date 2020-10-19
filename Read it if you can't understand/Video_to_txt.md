# Video_to_txt

## 1. CV2

pip install opencv

```
import cv2

vidcap = cv2.VideoCapture('005.avi')
success, image = vidcap.read()
```



## 2. 知识点

### 1）cv2.VideoCapture()

​		argument == 0 : open built-in camera

​		argument == path : open video 

​		use cap.release() to release after using it



### 2）acquire basic attribute

```
cap = cv2.VideoCapture(path)

cap.get(cv2.CAP_PROP_FRAME_COUNT)  # total frames
cap.get(cv2.CAP_PROP_FPS)		   # fps
cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # width
cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # height
```



### 2 ) convert to grayscale

```
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```



### 3) resize

```
image = cv2.resize(gray, size, interpolation=cv2.INTER_AREA) 
# interpolation defines the way in which it resizes
```



### 2)  videoWriter

​		creat a video

```
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编码格式
videoWriter = cv2.VideoWriter(storagePath + 'test.avi', fourcc, 30.0, (sourceImage.width, sourceImage.height))
# 输出视频参数设置,包含视频文件名、编码器、帧率、视频宽高(此处参数需和字符图片大小一致)
videoWriter.write(img)
```



### 3) os.path.abspath (".")

​		the absolute path of the py file



### 4) 将灰度与字符对应

```
# 灰度最大值255，以下两步意在将每个像素对应的值设为str中的下标
percents = img / 255
indexes = (percents * (len(str) - 1)).astype(numpy.int)
```



### 5) Convert PIL picture to CV2 picture

```
cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
```



### 6)video.write_videofile() 在未安装编码器时只能编码.mp4



### 7）tqdm 进度条

```
from tqdm import tqdm

# 每一次循环进度条进一
with tqdm(total=100) as pbar:
    for i in range(20):
    	# your code here
        time.sleep(1)
```



### 8）get BGM and combine it with the video

```
	# Get and save the BGM
	video = VideoFileClip(path)
    audio = video.audio
    audio.write_audiofile('tmp_music.mp3')

    # Combine audio and video
    video = VideoFileClip("silent.avi")
    audio_clip = AudioFileClip('tmp_music.mp3')
    video = video.set_audio(audio_clip)
    video.write_videofile("output.mp4")
```



### 9) delet temporary files

```
    if os.path.exists("tmp_music.mp3"):
        os.remove("tmp_music.mp3")
```

