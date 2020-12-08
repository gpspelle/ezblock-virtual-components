class Wheels():

    def __init__(self):
        print(" [.] Created left and right wheel in stop position")


    def stop(self):
        print(" [.] Stop wheels")


    def forward(self):
        print(" [.] Forward wheels")


    def right(self):
        print(" [.] Move right")
        

    def left(self):
        print(" [.] Move left")

    
    def backward(self):
        print(" [.] Move backward")


'''# Usage example
import time
wheels = Wheels()

wheels.forward()

time.sleep(5)
wheels.stop()

wheels.right()
time.sleep(2)

wheels.left()
time.sleep(2)

wheels.backward()

time.sleep(2)
wheels.stop()
'''
