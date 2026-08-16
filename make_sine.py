import numpy as np
def make_sine(f,duration,BITRATE,phase):
    duration=round(duration*f)/f
    samples = int(BITRATE * duration)

    data = np.zeros((samples, 2),dtype='float32')
    #the shape of the array has samples amount of rows
    times = np.linspace(0, duration, samples)  # x axis
    data[:samples, 0] = np.sin(times * f * 2 * np.pi)
    data[:samples, 1] = np.sin((times * f * 2 * np.pi)+phase)

    print(f"  {f} Hz      ", end='', flush=True)
    print(f"  {phase}/16                            ", end='\r', flush=True)
    return data, times