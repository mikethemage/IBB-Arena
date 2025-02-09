BOARD = 1
OUT = 1
IN = 1

def setmode(a):
    print(f"Set Mode: {a}")

def setup(a, b):
    print(f"Setup: {a}, {b}")

def output(a, b):
    print(f"Output: {a}, {b}")

class PWM:
    def __init__(self, pin, freq):
        print('PWM created on pin', pin, 'at frequency', freq)
    def start(self, duty):
        print('PWM started with duty cycle', duty)
    def ChangeDutyCycle(self, a):
        print(a)

def cleanup():
    print('Cleanup called')

def setwarnings(flag):
    print(f"Set warnings: {flag}")