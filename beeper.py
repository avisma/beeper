# beeper.py
# Ben Underwood

from winsound import Beep

# simple format example (notes will be played in a sequence):
# A A A A
# A B A B B A

# complex format:
# A1_1 (whole note A1)
# C#4_8 (eighth note C#4)
# Eb6_4. (dotted quarter note Eb6)

# complex format example (Twinkle, Twinkle):
# C4_4 C4_4 G4_4 G4_4 A4_4 A4_4 G4_2 F4_4 F4_4 E4_4 E4_4 D4_4 D4_4 C4_2 G4_4 G4_4 F4_4 F4_4 E4_4 E4_4 D4_2 G4_4 G4_4 F4_4 F4_4 E4_4 E4_4 D4_2 C4_4 C4_4 G4_4 G4_4 A4_4 A4_4 G4_2 F4_4 F4_4 E4_4 E4_4 D4_4 D4_4 C4_2

frequencies = {'D1': '36.71','D#1': '38.89','Eb1': '38.89','E1': '41.2','F1': '43.65','F#1': '46.25','Gb1': '46.25','G1': '49','G#1': '51.91','Ab1': '51.91','A1': '55','A#1': '58.27','Bb1': '58.27','B1': '61.74','C2': '65.41','C#2': '69.3','Db2': '69.3','D2': '73.42','D#2': '77.78','Eb2': '77.78','E2': '82.41','F2': '87.31','F#2': '92.5','Gb2': '92.5','G2': '98','G#2': '103.83','Ab2': '103.83','A2': '110','A#2': '116.54','Bb2': '116.54','B2': '123.47','C3': '130.81','C#3': '138.59','Db3': '138.59','D3': '146.83','D#3': '155.56','Eb3': '155.56','E3': '164.81','F3': '174.61','F#3': '185','Gb3': '185','G3': '196','G#3': '207.65','Ab3': '207.65','A3': '220','A#3': '233.08','Bb3': '233.08','B3': '246.94','C4': '261.63','C#4': '277.18','Db4': '277.18','D4': '293.66','D#4': '311.13','Eb4': '311.13','E4': '329.63','F4': '349.23','F#4': '369.99','Gb4': '369.99','G4': '392','G#4': '415.3','Ab4': '415.3','A4': '440','A#4': '466.16','Bb4': '466.16','B4': '493.88','C5': '523.25','C#5': '554.37','Db5': '554.37','D5': '587.33','D#5': '622.25','Eb5': '622.25','E5': '659.25','F5': '698.46','F#5': '739.99','Gb5': '739.99','G5': '783.99','G#5': '830.61','Ab5': '830.61','A5': '880','A#5': '932.33','Bb5': '932.33','B5': '987.77','C6': '1046.5','C#6': '1108.73','Db6': '1108.73','D6': '1174.66','D#6': '1244.51','Eb6': '1244.51','E6': '1318.51','F6': '1396.91','F#6': '1479.98','Gb6': '1479.98','G6': '1567.98','G#6': '1661.22','Ab6': '1661.22','A6': '1760','A#6': '1864.66','Bb6': '1864.66','B6': '1975.53','C7': '2093','C#7': '2217.46','Db7': '2217.46','D7': '2349.32','D#7': '2489.02','Eb7': '2489.02','E7': '2637.02','F7': '2793.83','F#7': '2959.96','Gb7': '2959.96','G7': '3135.96'}

def convertNoteComplex(value, bpm):
    note = value.split('_')
    note[0] = int(float(frequencies[note[0]]))

    lengths = {'1': 2000, '2': 1000, '4': 500, '8': 250, '16': 125} # for 120 BPM

    if bpm != 120:
        if bpm > 120:
            adjustbpm = 1 - (120 / bpm)
        else:
            adjustbpm = 120 / bpm
        
        for i in lengths:
            lengths[i] = lengths[i] * adjustbpm
        
    
    if '.' in note[1]:
        note[1] = int(lengths[note[1]] / 2)
        note[1] = int(note[1]) + int(lengths[note[1]])
    else:
        note[1] = int(lengths[note[1]])

    return note

def convertNoteSimple(value):
    if len(value) == 1:
        value = value + '4'
    value = int(float(frequencies[value]))
    return value

def main():
    mode = input("Simple or Complex mode? ")
    if "SIMPLE" in mode.upper():
        song = input("Enter notes: ")
        for i in range(len(song.split())):
            Beep(convertNoteSimple(song.split()[i]), 500)
    elif "COMPLEX" in mode.upper():
        bpm = int(input("BPM: "))
        song = str(input("Enter notes: "))
        for i in range(len(song.split())):
            Beep(convertNoteComplex(song.split()[i], bpm)[0], convertNoteComplex(song.split()[i], bpm)[1])
            
    #test = input("Note? ")
    #Beep(convertNote(test)[0], convertNote(test)[1])

def main2():
    # 120 BPM: 500ms per beat
    Beep(349, 1000)
    Beep(392, 250)
    Beep(415, 750)
    #
    Beep(466, 500)
    Beep(415, 250)
    Beep(466, 500)
    Beep(415, 250)
    Beep(466, 500)
    #
    Beep(523, 750)
    Beep(466, 250)
    Beep(415, 250)
    Beep(392, 500)
    Beep(349, 1250)

def main3():
    for i in range(100):
        Beep(349+2*i, 200)

while True:
    main()
