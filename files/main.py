import utime


rn = range(0,4)
r10 = range(0,50)
for i in rn:
    utime.sleep(0.5)
    print('hide')
    utime.sleep(0.5)
    print('show')
print('il')
print('pd')
for i in rn:
    print('f50')
    print('r90')
print('ul')
print('hide')
for i in r10:
    print('hide')
    #white cls line back
    print('scwhite\npw2\nr90\nf50')
    #goto front
    print('pu\nl90\nf51\nl90')
    #draw new pixel line black
    print('scblack\npd\nf50')
    #goback on the first line + 1 px
    print('pu\nl90\nf50\nr180\npd\npw1')

while True:
    print('hide')
    utime.sleep(0.1)
   
    utime.sleep(0.1)