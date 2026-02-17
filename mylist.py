from machine import Pin
import time

a=Pin(33,Pin.OUT)
b=Pin(5,Pin.OUT)
c=Pin(9,Pin.OUT)
d=Pin(18,Pin.OUT)

my_num = [[1,0,0,0],[0,1,0,0][0,0,1,0][0,0,0,1]]

for i in my_num:
    a.value(i[0])
    b.value(i[1])
    c.value(i[2])
    d.value(i[3])
    time.sleep(1)
