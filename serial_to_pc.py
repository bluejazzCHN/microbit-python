# 在这里写上你的代码 :-)
from microbit import *

def serial_init():
    uart.init(115200)

def command_control(status):

    if button_a.was_pressed():
        uart.write('Start to receive command:1.Left 2.Right \n\r')
        status = True
        sleep(100)
    if button_b.was_pressed():
        uart.write('Stop to receive command:\n\r')
        status = False
        sleep(100)
    return status

def command_action():
    if uart.any():
        command = uart.read()
        if int(command) == 1:
            display.show(Image.ARROW_W)
        elif int(command) == 2:
            display.show(Image.ARROW_E)

        uart.write('Temp:'+str(temperature())+'\n\r')
        uart.write('\n\r')
        sleep(500)

    if accelerometer.get_x() > 120:
        uart.write('X Turn Right:'+str(accelerometer.get_x())+'\n\r')
        sleep(200)
    elif accelerometer.get_x() < -120:
        uart.write('X Trun Left:'+str(accelerometer.get_x())+'\n\r')
        sleep(200)


serial_init()
start_status = False

while True:
    start_status = command_control(start_status)
    if start_status:
        command_action()
