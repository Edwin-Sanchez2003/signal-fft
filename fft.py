"""
    FFT

    Implements an FFT from a scratch.
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


def sine_signal_builder(
        freq  : float,  # sample rate, in Hz
        T_sec : float,  # period, in seconds
        N : int         # sample count (discrete values captured)
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



if __name__ == "__main__":
    main()
