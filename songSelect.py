from pygame import mixer
import random


HipHop80 = ["80sTrack1.mp3", "80sTrack2.mp3", "80sTrack3.mp3"]
countryHits = ["CountryTrack1.mp3", "CountryTrack2.mp3", "CountryTrack3.mp3"]
Pop2000 = ["Pop 1.mp3", "Pop 2.mp3", "Pop 3.mp3"]
modernHits = ["Modern1.mp3", "Modern2.mp3", "Modern3.mp3"]

# Cooper's functions start here
# ----------------------------

mixer.init()


def play80Hits():
    global currentSongList
    global songIndex
    currentSongList = "HipHop80"
    randomSong = random.randint(0, 2)
    songIndex = randomSong
    mixer.music.set_volume(mixer.music.get_volume())
    mixer.music.load(HipHop80[randomSong])
    mixer.music.play()


def playCountry():
    global currentSongList
    global songIndex
    currentSongList = "countryHits"
    randomSong = random.randint(0, 2)
    songIndex = randomSong
    mixer.music.set_volume(mixer.music.get_volume())
    mixer.music.load(countryHits[randomSong])
    mixer.music.play()


def play2000Pop():
    global currentSongList
    global songIndex
    currentSongList = "Pop2000"
    randomSong = random.randint(0, 2)
    songIndex = randomSong
    mixer.music.set_volume(mixer.music.get_volume())
    mixer.music.load(Pop2000[randomSong])
    mixer.music.play()


def playModernHits():
    global currentSongList
    global songIndex
    currentSongList = "modernHits"
    randomSong = random.randint(0, 2)
    songIndex = randomSong
    mixer.music.set_volume(mixer.music.get_volume())
    mixer.music.load(modernHits[randomSong])
    mixer.music.play()


def pause_song():
    mixer.music.pause()


def unpause_song():
    mixer.music.unpause()


def stop_song():
    mixer.music.stop()


def current_volume():
    return mixer.music.get_volume()


def turnitdown():
    mixer.music.set_volume(current_volume() - 0.1)


def turnitup():
    mixer.music.set_volume(current_volume() + 0.1)


def mute():
    mixer.music.set_volume(0)


def max_volume():
    mixer.music.set_volume(1)


def restart_song():
    mixer.music.rewind()


def quit_mixer():
    mixer.quit()


# Mason's functions start here
# ----------------------------

def nextSong():
    global songIndex
    global currentSongList
    songIndex += 1
    if songIndex >= len(Pop2000):
        songIndex = 0
    if currentSongList == "HipHop80":
        mixer.music.load(HipHop80[songIndex])
        mixer.music.play()
    elif currentSongList == "countryHits":
        mixer.music.load(countryHits[songIndex])
        mixer.music.play()
    elif currentSongList == "Pop2000":
        mixer.music.load(Pop2000[songIndex])
        mixer.music.play()
    elif currentSongList == "modernHits":
        mixer.music.load(modernHits[songIndex])
        mixer.music.play()


def previousSong():
    global songIndex
    global currentSongList
    songIndex -= 1
    if songIndex < 0:
        songIndex = 2
    if currentSongList == "HipHop80":
        mixer.music.load(HipHop80[songIndex])
        mixer.music.play()
    elif currentSongList == "countryHits":
        mixer.music.load(countryHits[songIndex])
        mixer.music.play()
    elif currentSongList == "Pop2000":
        mixer.music.load(Pop2000[songIndex])
        mixer.music.play()
    elif currentSongList == "modernHits":
        mixer.music.load(modernHits[songIndex])
        mixer.music.play()
