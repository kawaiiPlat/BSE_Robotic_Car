import picamera2
import cv2
import time
import math


def setup():
    time.sleep(0.5)


def runVision():
    ballLR = 0.50
    isBall = True
    # Slowly oscliate between left and right
    ballLR = math.sin(time.monotonic() / 2)
    return ballLR, isBall


if __name__ == "__main__":
    setup()
    while(True):
        print(runVision())
