import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd
import numpy as np
import keyboard as k
from scipy.fft import fft, fftfreq
import make_sine as m

BITRATE=96000
duration=0.1
running=True
f=440
period=1/f
phase=0
fig, ax = plt.subplots()

def up():
    global f
    f = f + 10

def down():
    global f
    if f>70:
        f=f-10

def out():
    global running
    running=False

def phase_up():
    global phase,data,line2
    if phase < (2 * np.pi):
        phase += (np.pi*2)/48
        data, times = m.make_sine(f, duration, BITRATE, phase)
        line2.set_ydata(data[:times.shape[0], 1])
        plt.draw()
def phase_down():
    global phase,data,line2
    if 0 < phase:
        phase -= (np.pi*2)/48
        data, times = m.make_sine(f, duration, BITRATE,phase)
        line2.set_ydata(data[:times.shape[0], 1])
        plt.draw()
def fft_process(data,samplerate):
    n=data.shape[0]
    yf = fft(data)
    xf = fftfreq(n, 1 / samplerate)
    #TODO:change pass into a return value
    pass
k.add_hotkey('right',up)
k.add_hotkey('left',down)
k.add_hotkey('q',out)
k.add_hotkey('a',phase_up)
k.add_hotkey('d',phase_down)
data, times = m.make_sine(f, duration, BITRATE, phase)
line,=ax.plot(times, data[:times.shape[0], 0])
line2,=ax.plot(times, data[:times.shape[0], 1])
plt.ion()
plt.show()

with sd.OutputStream(channels=2, samplerate=BITRATE) as stream:
    while running:
        data,t=m.make_sine(f,duration, BITRATE, phase)
        stream.write(data)
        plt.pause(0.001)
