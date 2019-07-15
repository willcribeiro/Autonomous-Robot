
from motorShield import MotorShield
import time, math, machine

def movimento():
    rodas = MotorShield()
    rodas.directionRobot(1, 1)
    rodas.vel(600,600)
    time.sleep(3)
    rodas.directionRobot(1, 0)
    rodas.vel(600,600)
    time.sleep(1)
    rodas.directionRobot(1, 1)
    rodas.vel(600,600)
    time.sleep(3)
    rodas.vel(0,0)