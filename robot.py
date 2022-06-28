import motor as m

class Robot:
    def __init__(self, mA_1: int = 31, mA_2: int = 33, mB_1: int = 35, mB_2: int = 37):
        self.mA = m.Motor(mA_1, mA_2)
        self.mB = m.Motor(mB_1, mB_2)
    
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