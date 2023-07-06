import time
import random
import winsound
import pywhatkit

def set_timer():
    timer = 0
    interval = int(input("What intervals do you want to work at?\n")) * 60
    # beep_time = random.randint(0, interval)
    beep_time = interval / 2
    timer_loop(timer, interval, beep_time)


def timer_loop(timer, interval, beep_time):
    while timer < interval:
        if beep_time == timer:
            winsound.Beep(1500, 500)
            # beep_time = random.randint(beep_time, timer)
            focus = input("Are you focused? (Y/N)\n")
            if focus in ["Y", "y"]:
                print("Good job!")
            elif focus in ["N", "n"]:
                print("Try again now!")
        time.sleep(1)
        timer += 1
        print(timer / 100)
    if timer == interval:
        reset_timer(timer)
        print("Time for a break!")
        time.sleep(5)
        break_time(interval / 4)


def break_time(break_timer):
    yt_player()
    timer = 0
    while timer < break_timer:
        time.sleep(1)
        timer += 1
        print(timer / 100)
    print("Time to work!")
    set_timer()


def reset_timer(timer):
    timer = 0


def yt_player():
    # put video links in the video array
    videos = ["https://www.youtube.com/watch?v=kcelgrGY1h8"]
    random_video = random.randint(0, len(videos) - 1)
    pywhatkit.playonyt(videos[random_video])


set_timer()
