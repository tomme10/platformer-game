import pygame
pygame.mixer.init()

channels = [pygame.mixer.Channel(i) for i in range(5)]

wind = pygame.mixer.Sound('Assets\\sounds\\wind.wav')
whiteNoise = pygame.mixer.Sound('Assets\\sounds\\whiteNoise.wav')
pinkNoise = pygame.mixer.Sound('Assets\\sounds\\pinkNoise.wav')

def play(sound,channel,loops = 0):
    channels[channel].play(sound,loops)

def pause(channel):
    channels[channel].pause()

def stop(channel):
    channels[channel].stop()

def stopAll():
    for channel in channels:
        channel.stop()

def setVolume(channel,volume):
    channels[channel].set_volume(volume)

def fade(channel,time):
    channels[channel].fadeout(time)
