import serial, pygame, time
pygame.init()

port = "COM3"
arduino = serial.Serial(port, 9600)
lx = 0.0
ly = 0.0
rx = 0.0
ry = 0.0
rt = 0.0
lt = 0.0
turning_sensitivity = 1.0
turning_deadzone = 0.1
main_j = pygame.joystick.Joystick(0)
main_j.init()

def create_game():
    print(main_j.get_numbuttons())
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("PythonRC")
create_game()

def process_speed(trigger_vector):
    return int(trigger_vector * 255)

def process_turning(turning_vector, speed):
    right = speed
    left = speed
    if turning_vector > (0.5 + turning_deadzone):
        left *= (1 - (turning_vector - 0.5) * 2) * turning_sensitivity
    elif turning_vector < (0.5 - turning_deadzone):
        right *= (1 - (turning_vector - 0.5) * -2) * turning_sensitivity
    return [int(left), int(right)]

run = True
while run:
    lx = round(main_j.get_axis(0), 1)
    ly = round(main_j.get_axis(1), 1)
    rx = round(main_j.get_axis(2), 1)
    ry = round(main_j.get_axis(3), 1)
    rt = round(main_j.get_axis(5) / 2 + 0.5, 1)
    lt = round(main_j.get_axis(4) / 2 + 0.5, 1)
    sp = process_speed(rt)
    motors = process_turning(lx / 2 + 0.5, sp)
    # print("Left x: " + lx, "Left y: " + ly, "Right x: " + rx, "Right y: " + ry, "Right trigger: " + rt, "Left trigger: " + lt)
    data = f"{str(motors[1])}|{str(motors[0])}"
    print(data)
    arduino.write(data.encode())
    # mx, my = pygame.mouse.get_pos()
    # mouse_pos = [int(mx  / (500 / 180)), int(my / (500 / 180))]
    # arduino.write(("X" + str(mouse_pos[0]) + "Y" + str(mouse_pos[1])).encode())
    # print("X" + str(mouse_pos[0]) + "Y" + str(mouse_pos[1]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(35)
pygame.quit()
