import visionShim as vs
import robot

if __name__ == "__main__":
    vs.setup()
    r = robot.Robot()

    while(True):
        ballLR, isBall = vs.runVision()
        print(f"{ballLR}, {isBall}")

        inp = input("Enter to continue, q to quit: ")
        if inp == "q":
            exit()