import machine
import utime
#800x800 display turtle screen
def a0(c):
    print(c)
for i in range(0,4):
    utime.sleep(1)
    a0('s')

c0=[ 
    'f800',
    'r90',
    ]
c=0
a0('pu')
a0('sg30')
a0('sb20')
a0('sc')
a0('gx400')
a0('gy400')
a0('gr')
a0('pd')
a0('il')
for i in range(0,len(c0)*4):
    c+=1
    if c==2:
        c=0
    a0(c0[c])
a0('ul')

while True:
    print('s')
    utime.sleep(0.5)
    print('h')
    utime.sleep(0.5)
    
