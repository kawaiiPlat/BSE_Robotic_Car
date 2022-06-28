import visionShim as vs
import robot
import time

if __name__ == "__main__":
    #vs.setup()

    r = robot.Robot(3,4,17,27)

    try:
        startTime = time.monotonic()
        runTime = time.monotonic() - startTime
        while(runTime < 10):
            ballLR, isBall = vs.runVision()

            message = ""
            if(ballLR < 0.4):
                r.turn(r.LEFT)
                message = "turning left "
            elif(ballLR > 0.6):
                r.turn(r.RIGHT)
                message = "turning right"
            else:
                r.stop()
                message = "Stopped      "
            runTime = time.monotonic() - startTime
            print("BallLR: {:.2f} | {} | {:.2f}".format(ballLR, message, runTime))
            time.sleep(0.1)

            r.stop()
    except TypeError as e:
        print(e)
    finally:
        r.stop()
        exit()
