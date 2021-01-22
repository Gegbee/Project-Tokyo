import serial, pygame, time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # physical pin numbering

pygame.init()

lx = 0.0
ly = 0.0
rx = 0.0
ry = 0.0
rt = 0.0
lt = 0.0

turning_sensitivity = 2.0 # 0-1 float
turning_deadzone = 0.1 # 0-1 float
turning_radius = 0.2 # 0-1 float
max_speed = 80 # 0-100 integer

turning_sensitivity = min(max(turning_sensitivity, 0.0), 1.0)
turning_radius = min(max(turning_radius, 0.0), 1.0)
turning_deadzone = min(max(turning_deadzone, 0.0), 1.0)
max_speed = min(max(max_speed, 0), 100)

main_j = pygame.joystick.Joystick(0)
main_j.init()

def create_pi():
    GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(36, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(38, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
    pwmSignalA = GPIO.PWM(31, 1000)
    pwmSignalB = GPIO.PWM(32, 1000)
    pwmSignalA.start(0)
    pwmSignalB.start(0)

def create_game():
    print(main_j.get_numbuttons())
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("PythonRC")
create_game()

def process_speed(trigger_vector):
    return int(trigger_vector * max_speed)

def process_turning(turning_vector, speed):
    turning_limit = float(speed * turning_radius)
    right = speed
    left = speed
    if turning_vector > (0.5 + turning_deadzone):
        left -= turning_limit
        left *= (1 - (turning_vector - 0.5) * 2) * turning_sensitivity
        left += turning_limit
        # left = max(left, turning_radius)
    elif turning_vector < (0.5 - turning_deadzone):
        right -= turning_limit
        right *= (1 - (turning_vector - 0.5) * -2) * turning_sensitivity
        right += turning_limit
        # right = max(right, turning_radius)
    return [int(left), int(right)]

run = True
while run:
    lx = round(main_j.get_axis(0), 1)
    ly = round(main_j.get_axis(1), 1)
    rx = round(main_j.get_axis(2), 1)
    ry = round(main_j.get_axis(3), 1)
    rt = round(main_j.get_axis(5) / 2 + 0.5, 1)
    lt = round(main_j.get_axis(4) / 2 + 0.5, 1)
    a = int(main_j.get_button(0))
    sp = process_speed(rt)
    motors = process_turning(lx / 2 + 0.5, sp)
    if motors[0] > 0:
        pwmSignalA.ChangeDutyCycle(motors[0])
    if motors[1] > 0:
        pwmSignalB.ChangeDutyCycle(motors[1])
    if a == 0:
        GPIO.output(35, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)
    else:
        GPIO.output(35, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)
    # print("Left x: " + lx, "Left y: " + ly, "Right x: " + rx, "Right y: " + ry, "Right trigger: " + rt, "Left trigger: " + lt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    time.sleep(0.1)
GPIO.cleanup()
pygame.quit()
