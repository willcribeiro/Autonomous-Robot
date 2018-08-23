from hcsr04 import HCSR04
from motorShield import MotorShield
import time, math, machine

sensor = HCSR04(trigger_pin=16, echo_pin=0)

servo = machine.PWM(machine.Pin(12), freq=50)

distance = sensor.distance_cm()

rodas = MotorShield()
rodas.directionRobot(1, 0)
rodas.vel(900,900)

i = 30
while True:
    print(distance)
    time.sleep(0.5)
    if distance<8:
        rodas.vel(0,0)
       
    else:
        rodas.vel(900,900)
        
