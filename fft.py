"""
    FFT

    Implements an FFT from a scratch.
    
    s(t) = A * cos(2 * pi * carrier_freq * time + phase)
    
    Cos -> in-phase, I(t)
    Sin -> quadrature, Q(t)
    NOTE: Phase-component is removed for IQ; they are locked at 90 degrees phase-shift.
    s(t) = I(t) * cos(2 * pi * carrier_freq * time) - Q(t) * sin(2 * pi * carrier_freq * time)
"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    fs_Hz : float = 40          # sample rate, in Hz
    T_sec : float = 1 / fs_Hz   # sample period, in seconds (time between each sample that is captured)
    N : int = 40                # sample count (discrete values captured)

    freq : float = 3            # signal frequency, in Hz
    t, A = sine_signal_builder(freq=freq, T_sec=T_sec, N=N)
    
    # Optional: plot
    plt.plot(t, A, marker='.', linestyle='-', color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Time Domain Signal')
    plt.show()

    IQ_example()


def sine_signal_builder(
        freq  : float,      # signal frequency, in Hz
        T_sec : float,      # period, in seconds (time between each sample that is captured)
        #duration : float,   # amount of time the signal should last for, in seconds.
        N : int             # sample count (discrete values captured)
) -> tuple [np.ndarray, np.ndarray ]:
    """
    Sine Signal Builder
    """
    # build the time component as a discrete vector.
    # the length of the vector is equal to the number of discrete samples we capture.
    # the values of each sample correspond to what to a value in time.
    t : np.ndarray = np.arange(0, N) * T_sec

    # build the Amplitude component as a discrete vector.
    # the length is equal to the time component vector.
    # the values correspond to to a sine wave.
    A : np.ndarray = np.sin(2 * np.pi * freq * t)
    return (t, A)


def one_sided_fft() -> None:
    pass


def IQ_example() -> None:
    fs = 1000          # Sampling rate
    t = np.arange(0, 1, 1/fs)  # 1 second of samples

    # Example: simple baseband modulation (sine)
    f_signal = 5  # 5 Hz baseband
    I = np.cos(2 * np.pi * f_signal * t)
    Q = np.sin(2 * np.pi * f_signal * t)

    f_carrier = 100  # Carrier frequency in Hz
    s = I * np.cos(2 * np.pi * f_carrier * t) - Q * np.sin(2 * np.pi * f_carrier * t)

    # NOTE: I, Q vectors can be whatever kind of data you want transferred - they're the data
    # component of the waveform. For instance, you would get those from QPSK or QAM

    plt.plot(t, I, label='I')
    plt.plot(t, Q, label='Q')
    plt.plot(t, s, label='Modulated Signal', alpha=0.6)
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
