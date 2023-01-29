import random


# Connor's code
# -----------------Function for Fuel Level---------------
def tire_pressure():
    PSI = random.uniform(32, 36)
    return PSI


# -----------------Function for Fuel Level--------------
def fuel_level():
    fl = random.randint(20, 100)
    return fl


# --------------Function for Engine Temp-------------------


def engine_temp(eng):
    num = random.randint(0, 1)
    temp = 82
    if num == 0:
        inctemp = random.uniform(0, 6)
        eng.set(f'{temp + inctemp:.1f} C')
    if num == 1:
        dectemp = random.uniform(0, 6)
        eng.set(f'{temp - dectemp:.1f} C')
