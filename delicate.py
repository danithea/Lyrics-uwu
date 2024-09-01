import sys
from time import sleep
import time

def lyrics():
    lines = [
        ("Sometimes I wonder, when you sleep", 0.1),
        ("Are you ever dreaming of me?", 0.11),
        ("Sometimes, when I look into your eyes", 0.11),
        ("I pretend you're mine, all the damn time...", 0.11),
        ("('Cause I like you)", 0.05),

        ("Is it cool that I said all that?", 0.07),
        ("Is it chill that you're in my head?", 0.06),
        ("'Cause I know that it's delicate", 0.06),

        ("(Delicate)", 0.05),
        ("(Yeah, I want you)", 0.05),

        ("Is it cool that I said all that?", 0.07),
        ("Is it too soon to do this yet?", 0.06),
        ("'Cause I know that it's delicate", 0.06),
        ("(Delicate <33)", 0.05),
    ]

    delays = (1.6, 1.8, 0.9, 1.7, 0.05, 
              0.115, 0.31, 1.5,
              0.1, 0.3, 
              0.12, 0.45, 1.65, 0.4)

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')


lyrics()