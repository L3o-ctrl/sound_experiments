import sounddevice as sd
import math
from numpy.ma.mrecords import addfield
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
fig2, ax2 = plt.subplots()
samplerate=48000 #samples/second (Hz=1/s)
# duration=0.01 # window time(s)
channels=1
sampInDur=4096#int(samplerate*duration) #samples in duration
def graph_update(yf):
    global fft_line
    fft_line.set_ydata(yf)
    plt.draw()

def fft_process(data,samplerate):
    n=data.shape[0]
    yf = fft(data)
    xf = fftfreq(n, 1 / samplerate) #1/ samplerate=time for one sample
    yf=np.absolute(yf)
    return yf, xf
def dom_freq(xf, yf):
    max_amp = np.argmax(yf)
    main_freq=xf[max_amp]
    return main_freq
def dom_note(freq):
    if freq>0:
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        note_number = 12 * math.log2(freq / 440) + 49
        note_number = round(note_number)
        note = (note_number - 1) % len(notes)
        note = notes[note]
        octave = (note_number + 8) // len(notes)
        return note, octave
    else:
        return None, None
data=np.zeros((sampInDur,channels)) #makes an array of length samples in duration
yf, xf=fft_process(data,samplerate) # defining xf and yf
fft_line,=ax2.plot(xf, yf, 'r')#creating fft_line on the figure
ax2.set_xlim(0,2048)
ax2.set_ylim(0,10)
plt.ion()
plt.show()
with sd.InputStream(channels=channels, samplerate=samplerate, blocksize=sampInDur) as stream:
    while True:
        data,overflow=stream.read(sampInDur)
        window = np.hanning(data.shape[0])
        data = data[:,0]*window
        #print(window.shape)
        yf,xf=fft_process(data, samplerate)
        main_freq=dom_freq(xf, yf)
        note, octave=dom_note(main_freq)
        #print(f"{main_freq} Hz                ",end="")
        print(f"{main_freq} Hz {note} {octave}               ",end="\r")
        graph_update(yf)
        plt.pause(0.1)

