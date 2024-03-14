from machine import Pin, PWM
from dcmotor import DCMotor
from time import sleep

capteur = Pin(16, Pin.IN)
buzzer = Pin(17,Pin.OUT)
frequency = 15000
pin15 = Pin(15, Pin.OUT)
pin14 = Pin(14, Pin.OUT)
enable = PWM(Pin(13), frequency)
dc_motor = DCMotor(pin15, pin14, enable)
btn = Pin(12,Pin.IN,Pin.PULL_DOWN)
red = Pin(19,Pin.OUT)
blue = Pin(18,Pin.OUT)

     
while 1:
    if not(capteur.value()):
        dc_motor.forward(100)
        red.value(1)
        blue.value(0)
        while btn.value() == 0:
            buzzer.high()
            sleep(1)
            buzzer.low()
            sleep(2)
    blue.value(1)
    red.value(0)
    dc_motor.stop()
    sleep(0.2)
