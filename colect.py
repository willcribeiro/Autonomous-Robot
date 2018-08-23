from hcsr04 import HCSR04
import time, math, machine

sensor = HCSR04(trigger_pin=16, echo_pin=0)
servo = machine.PWM(machine.Pin(12), freq=50)
distance = sensor.distance_cm()

i=30
servo.duty(30)

while i<136: #Giro do servo
    
            servo.duty(i)
            distance = sensor.distance_cm() #Leitura do sensor
            print('distancia',distance)
            time.sleep(1)
            i = i + 21 #Logica de rotação em 30 gráus