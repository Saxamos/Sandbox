import matplotlib.pyplot as plt

from scipy.io import wavfile

sampling_freq, signal_stereo = wavfile.read('data/NISSAN/accompaniment.wav')

mono_1 = signal_stereo[:, 0]
mono_2 = signal_stereo[:, 1]

fig, axs = plt.subplots(2, 2)
fig.suptitle('Spectrogram of the 2 stereo source of nissan accompaniment')
axs[0, 0].plot(mono_1)
axs[0, 0].set_ylim([-10000, 10000])
axs[0, 0].set(ylabel='Amplitude')
axs[1, 0].specgram(mono_1, Fs=sampling_freq)
axs[1, 0].set(xlabel='Time')
axs[1, 0].set(ylabel='Frequency')
axs[0, 1].plot(mono_2)
axs[0, 1].set_ylim([-10000, 10000])
axs[1, 1].specgram(mono_2, Fs=sampling_freq)
axs[1, 1].set(xlabel='Time')

plt.show()
