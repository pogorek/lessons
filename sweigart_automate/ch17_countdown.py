#! python3
# countdown.py - A simple countdown script.

import time
import subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['/mnt/c/Program Files (x86)/foobar2000/foobar2000.exe',
                  'automate_online-materials/alarm.wav'])
