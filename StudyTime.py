import time
import random
import winsound

def timer():
    timer = 0
    interval = int(input("What intervals do you want to work at?\n")) * 60
    beep_time = random.randint(0, interval)

    while timer < interval:
        if beep_time == timer:
            winsound.Beep(1500, 500)
            focus = input("Are you focused?")
            if focus == "y":
                print("Good job!")
            else:
                print("Try again now!")
        time.sleep(1)
        timer += 1
        print(timer / 100)
    if timer == interval:
        reset_timer(timer)
        print("Time for a break!")
        break_time(interval / 4)


def reset_timer(timer):
    timer = 0

def break_time(break_time):
    timer = 0

    while timer < break_time:
        time.sleep(1)
        timer += 1
        print(timer / 100)
    print("Time to work!")
    

timer()