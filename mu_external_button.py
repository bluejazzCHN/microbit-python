# 在这里写上你的代码 :-)
from microbit import *

pin1.set_pull(pin1.PULL_UP)

def check_pin_status(status):
    pin_status = status
    if pin1.is_touched:
        if pin_status == False:
            pin_status=True
        else:
            pin_status=False
    sleep(200)
    return pin_status

val = False
while True:
    val = check_pin_status(val)
    if val:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)


