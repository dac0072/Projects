from tkinter import (
    Button,
    Entry,
    Label,
    StringVar,
    Tk, Frame
)
import time
import volSelection
import songSelect
import Status
import navMod
import tkintermapview

# Dalton's code

def main():
    pass


# sets and displays time dynamically
def update():
    clock.config(text=time.strftime("%I:%M:%S %p"))
    clock.after(1000, update)


# clears both text fields
def clearField():
    e1.setvar("")
    e2.setvar("")


# changes font to black and deletes default message for 1st entry field
def temp_text1(e):
    e1.delete(0, 1000)
    e1.config(fg="black")


# changes font to black and deletes default message for 2nd entry field
def temp_text2(e):
    e2.delete(0, 1000)
    e2.config(fg="black")


if __name__ == "__main__":
    # GUI Initialization and Titling/Configuring
    Radiohead = Tk()
    Radiohead.title("Radiohead Main Menu")
    Radiohead.geometry("1180x700")
    Radiohead.config(bg="#88cffa")

    # Volume Selection Module - Buttons/labels
    vol = StringVar(Radiohead)
    vol.set("0.0")

    # Volume selection title label
    volSel = Label(Radiohead, text="Volume Selection", font=('Arial', 25, 'bold'), bg="#88cffa")
    volSel.grid(row=0, column=0)

    # Displays dynamic volume value
    volReturn = Label(Radiohead, textvariable=vol, bg="#88cffa")
    volReturn.grid(row=4, column=0)

    # Volume Up Button
    volUp = Button(Radiohead, text="+", width=5, height=1, command=lambda: volSelection.volUp(vol), font=('Arial', 15))
    volUp.grid(row=1, column=0)

    # Volume Down Button
    volDown = Button(Radiohead, text="-", width=5, height=1, command=lambda: volSelection.volDown(vol),
                     font=('Arial', 15))
    volDown.grid(row=3, column=0)

    # Mute Volume Button
    volMute = Button(Radiohead, text="mute", width=4, height=1, command=lambda: volSelection.volMute(vol),
                     font=('Arial', 15))
    volMute.grid(row=2, column=0)

    # Song Selection Module - Buttons/Labels
    songSel = Label(Radiohead, text="Song Selection/Control", font=('Arial', 25, 'bold'), bg="#88cffa")
    songSel.grid(row=6, column=0)

    # Genres title
    songChoice = Label(Radiohead, text="Genres", font=('Arial', 18), bg="#88cffa")
    songChoice.grid(row=7, column=0)

    # 80's hits play function
    song1 = Button(Radiohead, text="80's Hits", width=10, height=1, pady=10, command=songSelect.play80Hits)
    song1.grid(row=8, column=0)

    # Country hits play function
    song2 = Button(Radiohead, text="Country Hits", width=10, height=1, pady=10, command=songSelect.playCountry)
    song2.grid(row=9, column=0)

    # 2000s Pop play function
    song3 = Button(Radiohead, text="2000s Pop", width=10, height=1, pady=10, command=songSelect.play2000Pop)
    song3.grid(row=10, column=0)

    # Modern hits play function
    song4 = Button(Radiohead, text="Modern Hits", width=10, height=1, pady=10, command=songSelect.playModernHits)
    song4.grid(row=11, column=0)

    # Play Song button
    playSong = Button(Radiohead, text="Play Song", width=15, height=2, fg='green', command=songSelect.unpause_song)
    playSong.grid(row=13, column=0)

    # Pause Song button
    pauseSong = Button(Radiohead, text="Pause Song", width=15, height=2, fg='red', command=songSelect.pause_song)
    pauseSong.grid(row=14, column=0)

    # Replay Song button
    replaySong = Button(Radiohead, text="Replay", width=15, height=2, fg='orange', command=songSelect.restart_song)
    replaySong.grid(row=15, column=0)
    # Previous/Next Button Frame
    prevNext = Frame(Radiohead)
    prevNext.grid(row=16, column=0, columnspan=1)
    # Previous Song button
    prevSong = Button(prevNext, text="Previous", command=songSelect.previousSong)
    prevSong.grid(row=16, column=0)
    # Next Song button
    nextSong = Button(prevNext, text="Next", command=songSelect.nextSong)
    nextSong.grid(row=16, column=1)

    # Car Diagnostics/Status Module - Buttons/Labels
    carSens = Label(Radiohead, text="Car Diagnostics/Sensors", font=('Arial', 25, 'bold'), bg="#88cffa")
    carSens.grid(row=0, column=1)
    # Tire pressure label
    tpmsSens = Label(Radiohead, text="Tire Pressure", bg="#88cffa", font=('Arial', 15))
    tpmsSens.grid(row=1, column=1)
    # 4 car tire gauge labels
    label1 = Label(Radiohead, text=f'Tire 1: {Status.tire_pressure():.1f} PSI', bg="#88cffa")
    label1.grid(row=2, column=1)
    label2 = Label(Radiohead, text=f'Tire 2: {Status.tire_pressure():.1f} PSI', bg="#88cffa")
    label2.grid(row=3, column=1)
    label3 = Label(Radiohead, text=f'Tire 3: {Status.tire_pressure():.1f} PSI', bg="#88cffa")
    label3.grid(row=4, column=1)
    label4 = Label(Radiohead, text=f'Tire 4: {Status.tire_pressure():.1f} PSI', bg="#88cffa")
    label4.grid(row=5, column=1)

    # Fuel level title
    fuelLevel = Label(Radiohead, text="Fuel Level", bg="#88cffa", font=('Arial', 15))
    fuelLevel.grid(row=6, column=1)
    fuelLev = Status.fuel_level()

    # Display fuel level in red or green depending on value
    fuelDisplay = Label(Radiohead, text=f'{fuelLev:.0f}%', fg="blue", bg="#88cffa")
    if fuelLev >= 50:
        fuelDisplay.config(fg="green")
    else:
        fuelDisplay.config(fg="red")
    fuelDisplay.grid(row=7, column=1)
    # Engine temp title
    engTemp = Label(Radiohead, text="Engine Temperature", bg="#88cffa", font=('Arial', 15))
    engTemp.grid(row=8, column=1)
    # Displays variable engine temp which rises/fall with button keystroke
    eng = StringVar(Radiohead)
    eng.set("75.0 C")
    engDisplay = Label(Radiohead, textvariable=eng, bg="#88cffa")
    engDisplay.grid(row=9, column=1)

    # Updates engine temp when desired by user
    engStart = Button(Radiohead, text="Update Engine Temp", width=20, height=1, command=lambda: Status.engine_temp(eng))
    engStart.grid(row=10, column=1)

    # Navigation Module with distance measuring
    navHeader = Label(Radiohead, text="Navigation Control", font=('Arial', 25, 'bold'), bg="#88cffa")
    navHeader.grid(row=11, column=1)
    # Sets up timeToDest and distToDest as StrinVar for dynamic engine temp updates
    timeToDest = StringVar(Radiohead)
    distToDest = StringVar(Radiohead)
    timeToDest.set("")
    distToDest.set("")
    # Entry field for start and end destination
    e1 = Entry(Radiohead, width=40, fg="gray")
    e1.grid(row=13, column=1)
    e2 = Entry(Radiohead, width=40, fg="gray")
    e2.grid(row=14, column=1)
    # Enter/get eta and clear frame for buttons
    enternClear = Frame(Radiohead, bg="#88cffa")
    enternClear.grid(row=15, column=1, columnspan=2)
    clearField = Button(enternClear, text="Clear", command=lambda: navMod.clearField(e1, e2))
    clearField.grid(row=15, column=1)
    # Enter/Get ETA button
    distToDesti = Button(enternClear, text="Get ETA",
                         command=lambda: navMod.location2(distToDest, timeToDest, errDisplay, mapDisplay, e1, e2,
                                                          e1.get(), e2.get()))
    distToDesti.grid(row=15, column=0, padx=5)
    # Distance from destination display
    distDisplay = Label(Radiohead, textvariable=distToDest, bg="#88cffa", font=('Arial', 20))
    distDisplay.grid(row=19, column=1)
    # Time to end destination display
    timeDisplay = Label(Radiohead, textvariable=timeToDest, bg="#88cffa", font=('Arial', 20))
    timeDisplay.grid(row=20, column=1)
    # Displays errors as they are thrown in program runtime
    errDisplay = Label(Radiohead, text="", bg="#88cffa")
    errDisplay.grid(row=18, column=1)

    # Map for interactive use as well as location display
    mapDisplay = tkintermapview.TkinterMapView(Radiohead, width=400, height=300)
    mapDisplay.place(x=780, y=0)
    mapDisplay.set_address("345 W Magnolia Ave")

    # Allows for focus in and focus out manipulations
    e1.insert(0, "Start Location")
    e2.insert(0, "End Destination")
    mapDisplay.draw_rounded_corners()

    e1.bind("<FocusIn>", temp_text1)
    e2.bind("<FocusIn>", temp_text2)

    # creates a clock label to display time
    clock = Label(Radiohead, bg="#88cffa", foreground='black', font=('arial', 40, 'bold'))
    clock.grid(row=22, column=0)
    update()

    # ends the GUI main loop
    Radiohead.mainloop()
