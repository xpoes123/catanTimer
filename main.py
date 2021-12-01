import time
import keyboard

startTime = 900
increment = 10

st1 = startTime
p1 = "Player One: "
st2 = startTime
p2 = "Player Two: "
st3 = startTime
p3 = "Player Three: "
st4 = startTime
p4 = "Player Four: "

def countdown(t, p):
    while keyboard.is_pressed("p"):
        pass
    truth = True
    print("\n\n" + p)
    while truth:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(" " + timer, end="\r")
        for i in range(20):
            time.sleep(0.05)
            if keyboard.is_pressed('space'):
                print("\nTurn end")
                return t + increment
        t -= 1
        if t == 0:
            print(p + " flagged.")
            return 0

while(st1 != 0 or st1 != 0 or st3 != 0 or st4 != 0):
    st1 = countdown(st1, p1)
    st2 = countdown(st2, p2)
    st3 = countdown(st3, p3)
    st4 = countdown(st4, p4)