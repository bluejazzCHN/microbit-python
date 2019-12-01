from microbit import *

def DHT_query(data):
    humidity_high_bit = data[0:8]
    humidity_low_bit = data[8:16]
    temperature_high_bit = data[16:24]
    temperature_low_bit = data[24:32]
    check_bit = data[32:40]

    humi = 0
    humi_point = 0
    temp = 0
    temp_point = 0
    check = 0

    for i in range(8):
        humi += humidity_high_bit[i]*2**(7-i)
        humi_point += humidity_low_bit[i]*2**(7-i)
        temp += temperature_high_bit[i]*2**(7-i)
        temp_point += temperature_low_bit[i]*2**(7-i)
        check += check_bit[i]*2**(7-i)
    return humi, temp

def DHT11_init(pin):

    #MCU control info
    pin.write_digital(1)
    sleep(2000)
    pin.write_digital(0)
    sleep(18)
    pin.write_digital(1)
    sleep(0.04)

    data = []
    for i in range(0,40):
        data.append(pin.read_digital())

    return data


uart.init(115200)
pin8.set_pull(pin8.PULL_UP)
display.show('S')
while True:

    if button_b.was_pressed():
        data = DHT11_init(pin8)
        humi, temp = DHT_query(data)

        uart.write(str(humi)+':'+ str(temp)+'\n\r')
        display.scroll(str(humi))

