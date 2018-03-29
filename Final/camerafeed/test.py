
import os
import skvideo.io
videogen = skvideo.io.vreader('Test.mp4')
for frame in videogen:
        print(frame.shape)

