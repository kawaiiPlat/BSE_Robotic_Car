import RPi.GPIO as GPIO

# Call cleanup at the start to purge any other sessions effects
GPIO.cleanup()
# BCM means that you use the names of the GPIO pin numbers, not the actual pin numbers (e.g. use 3, aka GPIO3, for the pin at pin pos 5 from pinout)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, pin_1: int, pin_2: int):
        self.p1 = pin_1
        self.p2 = pin_2
        GPIO.setup(self.p1, GPIO.OUT)
        GPIO.setup(self.p2, GPIO.OUT)
        self.setSpeed(0)

    # Private method to set the pin states
    def __setPins(self, pin_1_state: bool, pin_2_state: bool):
        GPIO.output(self.p1, pin_1_state)
        GPIO.output(self.p2, pin_2_state)

    # Method to set the speed of the motors
    # @param speed: float, 0.0 means stop, 1.0 is full forward, -1.0 is full backwards
    def setSpeed(self, speed: float = 1.0):
        if(speed == 0):
            self.__setPins(0,0)
        if(speed > 0):
            self.__setPins(1,0)
        if(speed < 0):
            self.__setPins(0,1)

if __name__ == "__main__":
    m = Motor(3, 4)
    
    # No pins high
    m.setSpeed(0)
    input("stopped, press enter")

    # Pin 3 high
    m.setSpeed(1.0)
    input("forward, press enter")

    # Pin 4 high
    m.setSpeed(-1.0)
    input("backward, press enter")

    # No pins high
    m.setSpeed(0)
    input("stopped again, press enter")

    # if cleanup is called here, one of the motors starts turning with this pin setup.