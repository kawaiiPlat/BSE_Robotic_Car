import motor as m

class Robot:
    def __init__(self, mA_1: int = 31, mA_2: int = 33, mB_1: int = 35, mB_2: int = 37):
        self.mA = m.Motor(mA_1, mA_2)
        self.mB = m.Motor(mB_1, mB_2)
        
        # dependant on wire config
        # change the wires, not the code
        self.left = -1.0
        self.right = 1.0
        self.forwards = -1.0
        self.backwards = 1.0
    
    def __motorSpeed(self, mA_speed: float, mB_speed: float) -> None:
        self.mA.setSpeed(mA_speed)
        self.mB.setSpeed(mB_speed)

    # move forwards or backwards
    # @param speed: float, 0.0 means stop, 1.0 is full forward, -1.0 is full backwards
    def straight(self, speed: float) -> None:
        self.__motorSpeed(speed, speed)

    # spin left or right
    # @param speed: float, 0.0 means stop, 1.0 is full towards motor A, -1.0 is full towards motor B
    def turn(self, speed: float) -> None:
        self.__motorSpeed(-speed, speed)

    def stop(self) -> None:
        self.__motorSpeed(0.0, 0.0)

if __name__ == "__main__":
    r = Robot(3,4,17,27)

    r.stop()
    input("stopped, press enter")

    # No pins high
    r.straight(1.0)
    input("straight, press enter")

    r.straight(-1.0)
    input("Straight back, press enter")

    r.turn(1.0)
    input("Turning towards motor A, press enter")

    r.turn(-1.0)
    input("Turning towards motor B, press enter")

    r.stop()
    input("stopped, press enter")