from hcsr04 import HCSR04
from motorShield import MotorShield
import time, math, machine

sensor = HCSR04(trigger_pin=16, echo_pin=0)

servo = machine.PWM(machine.Pin(12), freq=50)

distance = sensor.distance_cm()

i = 30
while True:

    distance = sensor.distance_cm()
    print(distance)
    if distance<5:
        while i<136: 
            servo.duty(i)
            distance2 = sensor.distance_cm()
            print('distancia',distance2)
            time.sleep(1)
            print(i)
            i = i + 21

    else:
        i = 30
       
    
    
