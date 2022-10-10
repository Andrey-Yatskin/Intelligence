import numpy
import time
import random


def calcHist(mass):
    hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i < 1000000:
        if int(mass[i]) > 900:
            hist[9] += 1
        elif int(mass[i]) > 800:
            hist[8] += 1
        elif int(mass[i]) > 700:
            hist[7] += 1
        elif int(mass[i]) > 600:
            hist[6] += 1
        elif int(mass[i]) > 500:
            hist[5] += 1
        elif int(mass[i]) > 400:
            hist[4] += 1
        elif int(mass[i]) > 300:
            hist[3] += 1
        elif int(mass[i]) > 200:
            hist[2] += 1
        elif int(mass[i]) > 100:
            hist[1] += 1
        elif int(mass[i]) > 0:
            hist[0] += 1
        i += 1
    print(hist)


new_mass = numpy.random.random_integers(1, 999, 1000000)
calcHist(new_mass)



