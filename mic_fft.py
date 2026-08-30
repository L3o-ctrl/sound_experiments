import sounddevice as sd
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
fig2, ax2 = plt.subplots()
samplerate=96000
duration=0.2
channels=1
sampInDur=int(samplerate*duration)
def graph_update(yf):
    global fft_line
    fft_line.set_ydata(yf)
    plt.draw()

def fft_process(data,samplerate):
    n=data.shape[0]
    yf = fft(data)
    xf = fftfreq(n, 1 / samplerate)
    yf=np.absolute(yf)
    return yf, xf

data=np.zeros((sampInDur,channels))
yf, xf=fft_process(data,samplerate)
fft_line,=ax2.plot(xf, yf, 'c')
plt.ion()
plt.show()
with sd.InputStream(channels=channels, samplerate=samplerate, blocksize=sampInDur) as stream:
    while True:
        data,overflow=stream.read(sampInDur)
        yf,xf=fft_process(data, samplerate)
        graph_update(yf)
        plt.pause(0.001)

