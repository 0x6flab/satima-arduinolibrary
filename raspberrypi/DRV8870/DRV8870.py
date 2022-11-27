import RPi.GPIO as GPIO


class DRV8870:
    CLOCKWISE = 1
    COUNTERCLOCKWISE = 0
    COAST = 1
    BRAKE = 0
    _motor_count = None
    _motor_pin_1 = None
    _motor_pin_2 = None
    _motor_pin_3 = None
    _motor_pin_4 = None
    _M1 = None
    _M2 = None
    _M3 = None
    _M4 = None

    def __init__(self, motor_pin_1, motor_pin_2, frequency):
        # Assign motor
        self._motor_pin_1 = motor_pin_1
        self._motor_pin_2 = motor_pin_2
        # Set the motor count
        self._motor_count = 1
        # The GPIO Pin as output
        GPIO.setup(self._motor_pin_1, GPIO.OUT)
        GPIO.setup(self._motor_pin_2, GPIO.OUT)
        # Set the frequency for the PWM
        self._M1 = GPIO.PWM(self._motor_pin_1, frequency)
        self._M2 = GPIO.PWM(self._motor_pin_2, frequency)
        # Start the motors
        self._M1.start()
        self._M2.start()

    def __init__(
        self, motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4, frequency1, frequency2
    ):
        # Assign motor
        self.motor_pin_1 = motor_pin_1
        self.motor_pin_2 = motor_pin_2
        self.motor_pin_3 = motor_pin_3
        self.motor_pin_4 = motor_pin_4
        # Set the motor count
        self._motor_count = 2
        # The GPIO Pin as output
        GPIO.setup(self._motor_pin_1, GPIO.OUT)
        GPIO.setup(self._motor_pin_2, GPIO.OUT)
        GPIO.setup(self._motor_pin_3, GPIO.OUT)
        GPIO.setup(self._motor_pin_4, GPIO.OUT)
        # Set the frequency for the PWM
        self._M1 = GPIO.PWM(self._motor_pin_1, frequency1)
        self._M2 = GPIO.PWM(self._motor_pin_2, frequency1)
        self._M3 = GPIO.PWM(self._motor_pin_3, frequency2)
        self._M4 = GPIO.PWM(self._motor_pin_4, frequency2)
        # Start the motors
        self._M1.start()
        self._M2.start()
        self._M3.start()
        self._M4.start()

    def setSpeed(self, motor_speed, direction=CLOCKWISE):
        assert motor_speed >= 0 and motor_speed <= 100
        if self._motor_count == 1:
            if direction == self.CLOCKWISE:
                self._M1.ChangeDutyCycle(motor_speed)
                self._M2.ChangeDutyCycle(0)
            elif direction == self.ANTICLOCKWISE:
                self._M1.ChangeDutyCycle(0)
                self._M2.ChangeDutyCycle(motor_speed)
            else:
                pass
        elif self._motor_count == 2:
            if direction == self.CLOCKWISE:
                self._M1.ChangeDutyCycle(motor_speed)
                self._M2.ChangeDutyCycle(0)
                self._M3.ChangeDutyCycle(motor_speed)
                self._M4.ChangeDutyCycle(0)
            elif direction == self.ANTICLOCKWISE:
                self._M1.ChangeDutyCycle(0)
                self._M2.ChangeDutyCycle(motor_speed)
                self._M3.ChangeDutyCycle(0)
                self._M4.ChangeDutyCycle(motor_speed)
            else:
                pass
        else:
            pass

    def brake(self, mode=COAST):
        if self._motor_count == 1:
            if mode == self.COAST:
                self._M1.ChangeDutyCycle(0)
                self._M2.ChangeDutyCycle(0)
            elif mode == self.BRAKE:
                self._M1.ChangeDutyCycle(100)
                self._M2.ChangeDutyCycle(100)
            else:
                pass
        elif self._motor_count == 2:
            if mode == self.COAST:
                self._M1.ChangeDutyCycle(0)
                self._M2.ChangeDutyCycle(0)
                self._M3.ChangeDutyCycle(0)
                self._M4.ChangeDutyCycle(0)
            elif mode == self.BRAKE:
                self._M1.ChangeDutyCycle(100)
                self._M2.ChangeDutyCycle(100)
                self._M3.ChangeDutyCycle(100)
                self._M4.ChangeDutyCycle(100)
            else:
                pass
        else:
            pass
    
    
