# mini-projet
## capteur de flamme 

* capteur = Pin(16, Pin.IN)
* buzzer = Pin(17,Pin.OUT)
* frequency = 15000
* pin15 = Pin(15, Pin.OUT)
* pin14 = Pin(14, Pin.OUT)
* enable = PWM(Pin(13), frequency)
* dc_motor = DCMotor(pin15, pin14, enable)
* btn = Pin(12,Pin.IN,Pin.PULL_DOWN)
* red = Pin(19,Pin.OUT)
* blue = Pin(18,Pin.OUT)
* buzzer.low()