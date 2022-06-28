# BSE Robotic Car

Code created by Jarrod Sanders as an example for students of how to work with the Raspberry Pi's GPIO System


This code is designed to run on a Raspberry Pi 4B with OpenCV >= 4.6, PiCamera2, and the RPi.GPIO libraries


By default, pins (3,4) and (17,27) in the GPIO naming scheme are used to control a pair of h-bridges that are wired to motors on a 2wd robotic car.
visionShim.py provides a fake camera algorithm, as those will be highly custom to each user.
