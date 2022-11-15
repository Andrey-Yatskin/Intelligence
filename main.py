import math

def histDistance(hist1, hist2):
    i = 0
    distance = 0
    while i < n:
        distance = distance + math.pow(hist1[i], 2) + math.pow(hist2[i], 2)
        i += 1
    distance = math.sqrt(distance)
    print(distance)

def readHist(file):
    with open('hist') as file:
        lines = [line.rstrip() for line in file]
    hist1 = list(map(int, lines[0].split()))
    hist2 = list(map(int, lines[1].split()))
    file.close()
    return hist1, hist2

def writeHist(hist3, hist4):
    f = open('histForWrite', 'w')
    hist3 = " ".join(map(str, hist3))
    hist4 = " ".join(map(str, hist4))
    f.write(hist3 + '\n')
    f.write(hist4)
    f.close()

writeHist([1, 2, 4], [5, 6, 7])
hist1, hist2 = readHist('hist')

n = len(hist1)
m = len(hist2)
if m != n:
    print('Enter histogram the same lenght')
    exit()

histDistance(hist1, hist2)