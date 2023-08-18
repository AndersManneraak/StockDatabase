import time
import os
import pandas as pd

class Timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print(self.message)
        print(time.time() - self.start)