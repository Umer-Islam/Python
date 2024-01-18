direction = input("enter left or right")

if direction == 'left':
    swin_wait = input("swin or wait?")
    if swin_wait == "wait":
        door = input('select the door')
        if door == 'yellow':
            print('you WON')
        else:
            print('game over3')
    else:
        print('game over2')
else:
    print('game over1')
    