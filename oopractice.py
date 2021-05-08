
######################################################
class SerialGenerator:
    """Machine to create unique incrementing serial numbers. 2 methods"""
    def __init__(self, start=0):
        if not isinstance(start, int):
            raise ValueError("Not an integer")
        self.start = start
        self.value = start

    def generate(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = self.start

serial = SerialGenerator(start=1000)
serial.reset()
serial.generate()
serial = SerialGenerator(start=4.3)
serial = SerialGenerator(start="hi")

######################################################
import os
import random

class RandomWord:
    _FILEPATH = os.path.join(os.curdir,"ignoreland","words.txt")
    _SEED = 8675309

    def __init__(self, filepath=RandomWord._FILEPATH):
        file = open(filepath)
        self.wordlist = file.read(500000).split("\n")
        # self.wordlist = self.getwords(file)  # alternatively
        print(str(len(self.wordlist)) + " words read")

    def getwords(self, file):
        wordlist = file.read(500000).split("\n")
        return wordlist

    def random(self):
        return random.choice(self.wordlist)

wf = RandomWord()
wf.random()

