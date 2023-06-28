import machine
import utime

for d in range(0,7):
    print('s')
    utime.sleep(1)

machine.Pin(25,machine.Pin.OUT).on()
for i in range(0,180):
    print('f005')
    print('r009')
    print('f001')
    print('r009')
    print(i)

machine.Pin('LED',machine.Pin.OUT).value(0)

while True:
    print("h")
    utime.sleep(0.1)
    
