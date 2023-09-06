# import module
from playsound import playsound
import time
import os

CLEAR = "\033[2J" # clearing the terminal screen
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    # Track of time how much time elapsed
    time_elapsed = 0
    print(CLEAR)  #clearing the terminal screen

    while time_elapsed < seconds:
        time.sleep(1) # wait for 1 second. Just pause the code right here wait for a second and it will continues.
        time_elapsed += 1 # increment the plus one

        time_left = seconds - time_elapsed # to find the time left
        minutes_left = time_left // 60 # to find minutes left
        seconds_left = time_left % 60  # to find the seconds left

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("/home/dckapl108/Desktop/Files/python/projects/Alarm Clock/AlarmSounds/mixkit-facility-alarm-sound-999.wav")

minutes = int(input("How many Minutes to wait: "))
seconds = int(input("How many Seconds to wait: "))
total_Seconds = minutes * 60 + seconds
alarm(total_Seconds)

