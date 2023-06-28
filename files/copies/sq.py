import machine
import utime


for i in range(0,4):
    utime.sleep(0.5)
    print('s')
    utime.sleep(0.5)
    print('h')
    
for i in range(0,100):
    print('f'+str(i))
    print('r90')
machine.Pin(25,machine.Pin.OUT).value(1)

while True:
    utime.sleep(0.5)
    print('s')
    utime.sleep(0.5)
    print('h')
