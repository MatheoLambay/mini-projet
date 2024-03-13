from machine import Pin, PWM
from dcmotor import DCMotor
from time import sleep


capteur = Pin(16, Pin.IN)

frequency = 15000
pin15 = Pin(15, Pin.OUT)
pin14 = Pin(14, Pin.OUT)
enable = PWM(Pin(13), frequency)
dc_motor = DCMotor(pin15, pin14, enable)
btn = Pin(17,Pin.PULL_DOWN)

while 1:
    if not(capteur.value()):
        while not(btn.value()):
            dc_motor.backwards(100)
    dc_motor.stop()
    sleep(0.2)    
    