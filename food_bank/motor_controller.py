from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory

TREADMILL_MOTOR_PIN = 5

ROD_MOTOR_PIN = 12
ROD_MOTOR_STATE_1 = 0.5
ROD_MOTOR_STATE_2 = 1

class MotorController:
    
    # Class to deal with controlling all motors
    def __init__(self):
        self.treadmill_motor = Servo(TREADMILL_MOTOR_PIN)
        self.rod_motor = Servo(ROD_MOTOR_PIN,
                                # min_pulse_range=0.0005,
                                # max_pulse_range=0.0025,
                                pin_factory=factory)
        
    def stop_treadmill(self):
        assert False
        
    def start_treadmill(self):
        assert False
        
    def rod_motor_to_first_state(self):
        self.rod_motor.value = ROD_MOTOR_STATE_1
         
    def rod_motor_to_second_state(self):
        self.rod_motor.value = ROD_MOTOR_STATE_2


motor_controller = MotorController()
while True:
    motor_controller.rod_motor_to_first_state()
    sleep(1)
    # motor_controller.rod_motor_to_second_state()
    # sleep(1) 
    
"""
servo = Servo(17)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)

"""
