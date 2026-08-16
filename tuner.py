import make_sine as m
import matplotlib.pyplot as plt
import numpy as np
import keyboard as k
from scipy.fft import fft, fftfreq
# fft link https://realpython.com/python-scipy-fft/
fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
ax2.set_xlim(0, 5000)
ax2.set_ylim(0,200)
f=440
period=1/f
phase=0
samplerate=96000
duration=0.1
"""goals:
1.make the fft plot
2.add code for microphone to record sound
3.check recorded frequency for tuning
"""
def phase_up():
    global phase, data, line2
    if phase < (2 * np.pi):
        phase += (np.pi * 2) / 48
        data, times = m.make_sine(f, duration, samplerate, phase)
        line2.set_ydata(data[:times.shape[0], 1])
        plt.draw()
def phase_down():
    global phase, data, line2
    if 0 < phase:
        phase -= (np.pi*2)/48
        data, times = m.make_sine(f, duration, samplerate, phase)
        line2.set_ydata(data[:times.shape[0], 1])
        plt.draw()
def fft_process(data,samplerate):
    n=data.shape[0]
    yf = fft(data)
    xf = fftfreq(n, 1 / samplerate)
    return yf, xf
def up():
    global f
    f = f + 10
def down():
    global f
    if f>70:
        f=f-10
k.add_hotkey('right',up)
k.add_hotkey('left',down)
k.add_hotkey('a',phase_up)
k.add_hotkey('d',phase_down)
data, times = m.make_sine(f, duration, samplerate, phase)
line,=ax.plot(times, data[:times.shape[0], 0],'x')
line2,=ax.plot(times, data[:times.shape[0], 1])
yf, xf = fft_process(data[:times.shape[0], 0]*2,samplerate)
#TODO:Add frequency change(done)
#TODO:make the fft plot realtime
#TODO:change the fft plot to show only 0-5000(done)
fft_line,=ax2.plot(xf,yf,'x')
plt.ion()
plt.show()
while True:
    plt.pause(0.001)