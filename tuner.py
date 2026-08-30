import make_sine as m
import matplotlib.pyplot as plt
import numpy as np
import keyboard as k
from scipy.fft import fft, fftfreq

"""
1)  make sure you can complete both a flowchart and the event graph (usage graph)p
2)  explain the difference between the output/effects/consequence ax.plot, make_sine/fft, linex.set_ydata
"""


# fft link https://realpython.com/python-scipy-fft/

#fig, ax = plt.subplots()# fig=window gen/ ax=buttons etc.
fig2, ax2 = plt.subplots()
f=440
period=1/f
phase=0
samplerate=96000
duration=0.1

#ax.set_xlim(0,(period*2))#makes sine graph the length of two periods for easier reading
ax2.set_xlim(0, 500)#fft graph x range
# ax2.set_ylim(0,8)#fft graph y range
"""goals:
1.make the fft plot
2.add code for microphone to record sound
3.check recorded frequency for tuning
"""
def graph_update():
    global data, times, line2, line, xf, yf, samplerate, phase, f, duration, fft_line
    data, times = m.make_sine(f, duration, samplerate, phase)#sets data+times to the output values of make_sine
    yf, xf = fft_process(data[:times.shape[0], 1], samplerate)
    # yf=np.absolute(yf)

    # yf, xf = fft_process(data[:times.shape[0], 1], samplerate)
    # n=data.shape[0]#Length of data array
    # yf = fft(data[0])#output of fft on data array
    # xf = fftfreq(n, 1 / samplerate)#sampletime(time for 1 sample)
    # fft_line, = ax2.plot(xf, yf, 'c')
    #line vs line 2
    #line is channel 0 sine wave line & line2 is channel 1
    #line.set_ydata(data[:times.shape[0], 0])
    #line2.set_ydata(data[:times.shape[0], 1])
    # fft channel vvv
    fft_line.set_ydata(yf)#value to put for set_ydata?
    plt.draw()
def phase_up():
    global phase, data, line2
    if phase < (2 * np.pi):
        phase += (np.pi * 2) / 48
        graph_update()
        # data, times = m.make_sine(f, duration, samplerate, phase)
        # line2.set_ydata(data[:times.shape[0], 1])
        # plt.draw()
def phase_down():
    global phase, data, line2
    if 0 < phase:
        phase -= (np.pi*2)/48
        graph_update()
        # data, times = m.make_sine(f, duration, samplerate, phase)
        # line2.set_ydata(data[:times.shape[0], 1])
        # plt.draw()
def fft_process(data,samplerate):
    n=data.shape[0]
    yf = fft(data)
    xf = fftfreq(n, 1 / samplerate)
    # graph_update()
    return np.absolute(yf), xf
def freq_up():
    global f
    f = f + 10
    # plt.draw()
    graph_update()
def freq_down():
    global f
    if f>70:
        f=f-10
    # plt.draw()
        graph_update()
k.add_hotkey('right', freq_up)
k.add_hotkey('left', freq_down)
k.add_hotkey('a',phase_up)
k.add_hotkey('d',phase_down)
#next 2 lines are sine wave
data, times = m.make_sine(f, duration, samplerate, phase)
#line,=ax.plot(times, data[:times.shape[0], 0])#line for channel 0
#line2,=ax.plot(times, data[:times.shape[0], 1],'g')#line for channel 1
#TODO:Add frequency change(done)
#TODO:make the fft plot realtime
# still not updating fft plot
#TODO:change the fft plot to show only 0-5000(done)
yf, xf = fft_process(data[:times.shape[0], 1],samplerate)#
fft_line,=ax2.plot(xf, yf, 'c')
plt.ion()
plt.show()
while True:
    # plt.draw()
    plt.pause(0.001)
