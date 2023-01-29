from pygame import mixer

# Mason's code
mixer.init()
mixer.music.set_volume(0.5)


# returns the volume
def returnVol():
    return mixer.music.get_volume()


# increases the volume
def volUp(vol):
    currentVol = mixer.music.get_volume()
    mixer.music.set_volume(currentVol + 0.1)
    vol.set(mixer.music.get_volume())


# decrease the volume
def volDown(vol):
    currentVol = mixer.music.get_volume()
    mixer.music.set_volume(currentVol - 0.1)
    vol.set(mixer.music.get_volume())


# sets volume to 0
def volMute(vol):
    mixer.music.set_volume(0)
    vol.set(mixer.music.get_volume())
