# Python Pillow

from PIL import pillow

## 1、基本操作

```
from PIL import Image
image = Image.open('image.jpg')
image.show()
```

### 1）新建

```
image.new('RGB',(160, 90), (0, 0, 255))
#(0,0,255) can be replaced by '#0000FF' or 'blue'
```

### 2)拷贝和保存

```
# 拷贝和保存
image = Image.open("yazi.jpg")
image_copy = image.copy()
# image_copy.show()
image_new = Image.new('RGB', (160, 90), (0, 0, 255))
image_new2 = Image.new('L', (160, 90), '#646464')
image_copy.paste(image_new, (100, 100, 260, 190), mask=image_new2)
image_copy.save('duck.jpg')
image_save = Image.open('duck.jpg')
print(image_save.format, image_save.mode)
image_copy.show()
```

mask, 蒙版。传入一张与被粘贴图片尺寸一样的图片，可以使用模式为'1'、'L'或者'RGBA'的图像。如果mask图像的颜色值为255，则直接按被粘贴图片的颜色粘贴，如果mask图像的颜色值为0，则保留当前图片的颜色(相当于没有粘贴)，如果mask图像的颜色值为0~255之间的值，则将im与mask进行混合后再粘贴。

### 3）裁剪和缩放

```
image_crop = image.crop(box = (100, 100, 100, 100))
image_resize = image.resize((500, 400), resample=Image.LANCZOS, box=(100, 100, 1200, 800), reducing_gap=5.0)
```

### 1) box

box表示裁剪的区域，传入长度为4的元组(

### 2)resize(size, resample=BICUBIC, box=None, reducing_gap=None)



## 2、常用属性

```
image.width
image.height
image.size      # =(image.width, image.height)
image.mode		# 1, L, P, RGB, RGBA, CMYK, YCbCr, I, F
image.format    # eg. jpg.
image.readonly  # is_read_only, a boolean
image.info      # a dict containing the pic's information
```

### 1)image.mode:

​	There are 9 modes in PIL: 1, L, P, RGB, RGBA, CMYK, YCbCr, I, F

​	模式“1”为二值图像，非黑即白。但是它每个像素用8个bit表示，0表示黑，255表示白。

​	模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的
 L = R * 299/1000 + G * 587/1000+ B * 114/1000

​	模式“P”为8位彩色图像，它的每个像素用8个bit表示，其对应的彩色值是按照调色板查询出来的。

​	模式“RGBA”为32位彩色图像，8bit透明通道。

​	模式“CMYK”为32位彩色图像，印刷

​	模式“YCbCr”为24位彩色图像，彩色视频格式

​	模式“I”为32位整型灰色图像，I = R * 299/1000 + G * 587/1000 + B * 114/1000

​	模式“F”为32位浮点灰色图像，F = R * 299/1000+ G * 587/1000 + B * 114/1000，模式“F”与模式“L”的转换公式是一样的，都是RGB转换为灰色值的公式，但模式“F”会保留小数部分.

​	模式“RGB”为24位彩色图像
​	在PIL中，对于彩色图像，open后都会转换为“RGB”模式，然后该模式可以转换为其他模式，比如“1”、“L”、“P”和“RGBA”，这几种模式也可以转换为“RGB”模式。

### 2）模式转换

```
im = Image.open('image.jpg')
im1 = im.convert('L')
# convert(self, mode=None, matrix=None, dither=None, palette=WEB, colors=256):
```



## 3、图片缩放

thumbnail 缩略图

```
from PIL import Image

im = Image.open('image.jpg')
wide, height = im.size
im.thumnail((wide // 2, height // 2))  
im.save('thumbnail.jpg','jpeg')
```



## 4、模糊

filter 滤镜    blur 模糊

```
from PIL import Image, ImageFilter
im = Image.open('image.jpg')
im2 = im.ilter(Imagefilter.BLUR)
im2.save('blur.jpg','jpeg')
```



## 5、获取每个像素的RGB值

#### im.getdata()函数的返回值是一个sequence对象，sequence对象的每一个元素对应一个像素点R、G、B值

每个对象:RGB下为(0,0,255),L或P模式下为一个整型值



## 6、绘制字符串

```
ImageDraw.multiline_text(xy,text,fill=None,font=None,anchor=None,spacing=0,align="left",direction=None,features=None)
# or: ImageDraw.text(the same as above)
```

- **xy** -- 文本的左上角。
- **text** -- 要绘制的文本。
- **fill** -- 用于文本的颜色。
- **font** -- 安 [`ImageFont`](https://www.osgeo.cn/pillow/reference/ImageFont.html#PIL.ImageFont.ImageFont) 实例。
- **spacing** -- 行与行之间的像素数。
- **align** -- `"left"` ， `"center"` 或 `"right"` .
- **direction** -- 文本的方向。它可以 `"rtl"` （从右到左）， `"ltr"` （从左到右）或 `"ttb"` （从上到下）。需要libraqm

```
from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (300, 300), 0)

# 创建可绘制的对象
draw = ImageDraw.Draw(im)
# 设置字体，将字体库复制到当前目录
font = ImageFont.truetype('arialbi.ttf', 32)
# 填充文字
draw.multiline_text((10,10), "Hello,\nwoodman", font=font, fill="#FFFFFF")
```

