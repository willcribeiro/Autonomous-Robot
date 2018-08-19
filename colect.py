from hcsr04 import HCSR04
import time, math, machine

sensor = HCSR04(trigger_pin=16, echo_pin=0)
servo = machine.PWM(machine.Pin(12), freq=50)
i = 30
#Leitura em 180 graus
while i<136: 
    print(i)
    servo.duty(i)
    time.sleep(1)
    i = i + 21


    
    
