# timer.py

import time
import sys

def countdown(seconds):
    """
    Countdown timer for the question.
    Displays the remaining time in seconds.
    """
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\rTime left: {remaining} seconds ")
        sys.stdout.flush()
        time.sleep(1)
    print("\n⏳ Time's up!")
