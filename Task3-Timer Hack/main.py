'''
To set timer and sing the alarm
'''
from time import sleep
from playsound import playsound
import platform
import os

def play_alarm(path):
    playsound(path)

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    song = 'alert.mp3'
    path = f'./assets/tones/{song}'
    duration = int(input("Enter Duration in seconds: "))
    while duration:
        clear_screen()
        if(duration < 5):
            print('About to finish!')
        elif(duration < 10):
            print('Almost finished!')
        print(f'{duration} seconds remaining')
        sleep(1)
        duration -= 1
    clear_screen()
    print('Time is up!')
    play_alarm(path)