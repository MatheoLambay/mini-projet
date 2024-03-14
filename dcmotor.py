from machine import Pin, PWM

class DCMotor:
    def __init__(self, pin1, pin2, enable_pin, min_duty=0, max_duty=65535):
        self.pin1=pin1
        self.pin2=pin2
        self.enable_pin=enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

    def forward(self,speed):
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        #self.enable_pin.duty_u16(32768)
        self.pin1.value(0)
        self.pin2.value(1)

    def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def stop(self):
        self.enable_pin.duty_u16(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def duty_cycle(self, speed):
        
        if self.speed <= 0 or self.speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
        return duty_cycle