import mss
from PIL import Image
from time import perf_counter as T
left  = 0
right = 200
top   = 0
btm   = 200

with mss.mss() as sct:
    monitor = sct.monitors[1]
    bbox    = (left, top, right, btm)

    sT=T()
    sct_im = sct.grab(bbox) # type <class 'mss.screenshot.ScreenShot'>
    eT=T();print(" >", eT-sT)
    
    # Create the Image
    img = Image.frombytes("RGB", sct_im.size, sct_im.bgra, "raw", "BGRX")
    img.show()