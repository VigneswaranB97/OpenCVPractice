# Day 2

``` Working On Videos: ```
* Reading and writing Video.
* Avi to mp4 and vise versa.
* Getting FPS.
* Getting size.

## For VideoWriter class, There are several Video Codec

 ```The available codecs may vary from system to system. Options include: ```

* **cv2.VideoWriter_fourcc('I','4','2','0')** : This is an uncompressed YUV, 4:2:0 chroma subsampled. This encoding is widely compatible but produces large files. The file extension should be avi. 
* **cv2.VideoWriter_fourcc('P','I','M','1')**: This is MPEG-1. The file extension should be avi. 
* **cv2.VideoWriter_fourcc('M','J','P','G')**: This is motion-JPEG. The file extension should be avi. 
* **cv2.VideoWriter_fourcc('T','H','E','O')**: This is Ogg-Vorbis. The file extension should be ogv. 
* **cv2.VideoWriter_fourcc(cv.CV_FOURCC('F','L','V','1')**: This is Flash video. The file extension should be flv. 
