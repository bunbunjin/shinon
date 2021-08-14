import pygame
import time
from dataclasses import dataclass


# range [bpm : bpm+20]
def timing(bpm):
    num = 60 / bpm
    print(num)
    print(int(num))
    return num


def heartbeat(bpm):
    num = timing(bpm)
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load('shinon_model.wav')
    pygame.mixer.music.play(1)
    time.sleep(num)
    pygame.mixer.music.stop()


def repeat(bpm):
    init = bpm
    _bpm = bpm + 20
    while True:
        while _bpm >= bpm:
            bpm += 1
            heartbeat(bpm)
            print(_bpm)
            print(bpm)
        else:
            while init <= bpm:
                bpm -= 1
                heartbeat(bpm)
                print(_bpm)
                print(bpm)


repeat(60)
