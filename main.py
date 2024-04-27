from machine import Pin, PWM
from dcmotor import DCMotor
import uasyncio 
#code capteur de flamme by
#Lambay Mathéo
#Ouaffi Zakaria

class FireDetector:
    def __init__(self,Pin_capteur,Pin_buzzer,Pin_btn,Pin_red,Pin_green,Pin_forward,Pin_backward,Pin_enable): 
        self.capteur = Pin(Pin_capteur, Pin.IN)
        self.buzzer = Pin(Pin_buzzer,Pin.OUT)
        self.Pin_forward = Pin(Pin_forward,Pin.OUT)
        self.Pin_backward = Pin(Pin_backward,Pin.OUT)
        self.enable = PWM(Pin(Pin_enable),15000)
        self.dc_motor = DCMotor(self.Pin_forward,self.Pin_backward,self.enable)
        self.button = Pin(Pin_btn,Pin.IN,Pin.PULL_DOWN)
        self.red = Pin(Pin_red,Pin.OUT)
        self.green = Pin(Pin_green,Pin.OUT)
        #mise à zéro des variables et des actionneurs 
        self.buzzer.low()
        self.green.high()
        self.red.low()
        self.dc_motor.stop()
        self.isFire = 0

    async def detectFire(self): #passe le flag isFire sur 1 lorsque la flamme est détecté
        while 1:
            if not(self.capteur.value()): 
                self.isFire = 1
            await uasyncio.sleep(0.1)

    async def ventillo(self): #allume le ventillo ou l'arrête
        while 1:
            if self.isFire:
                self.dc_motor.forward(100)
            else:
                self.dc_motor.stop()
            await uasyncio.sleep(0.1)

    async def btnPressed(self): # reset du flag isFire
        while 1:
            if self.button.value():
                self.isFire = 0  
            await uasyncio.sleep(0.1)

    async def ledOn(self): #gère la couleur de la led RGB
        while 1:
            if self.isFire:
                self.green.low()
                self.red.high()
            else:
                self.green.high()
                self.red.low()
            await uasyncio.sleep(0.1)

    async def buzzerOn(self): #fait bipper le buzzer toutes les secondes
        while 1:
            if self.isFire:
                self.buzzer.high()
                await uasyncio.sleep(1)
                self.buzzer.low()
                await uasyncio.sleep(1)
            else:
                self.buzzer.low()
            await uasyncio.sleep(0.1)

async def main(): #initialisation du capteur et appelle des fonction asynchrone. 
    capteur = FireDetector(16,17,12,19,18,15,14,13)
    while 1:
        uasyncio.create_task(capteur.detectFire())
        uasyncio.create_task(capteur.ventillo())
        uasyncio.create_task(capteur.btnPressed())
        uasyncio.create_task(capteur.ledOn())
        uasyncio.create_task(capteur.buzzerOn())
        await uasyncio.sleep(10)

uasyncio.run(main())