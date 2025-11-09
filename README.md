# Signals - FFT
Perform FFT, from scratch, in python.


## Environment Setup

1. `conda create -n fft python=3.14 -y`
2. `conda activate fft`
3. `pip install -r requirements.txt`

## Documentation
* [Scipy-Signal](https://docs.scipy.org/doc/scipy/reference/signal.html)
* [Dataset GitHub](https://github.com/JaronFontaine/Sub-GHz-IQ-signals-dataset?tab=readme-ov-file)
* [Datset Webpage](https://cloud.ilabt.imec.be/index.php/s/bqXtdp9QsfXLbb3)

## ToDo
* Consider making a Class to build signals:
  * return a time array, amplitude array to represent the signal
  * provide signal contextual data (frequency? time period? etc.)
  * signal object has functions to return the signal with different representations.
* make a facade around matplotlib for signals, providing plotting options for signals.
* add open-source license to repo.
* add amplitude as a vector (for dynamic adjustments of amplitude)
* add frequency as a vector (foy dynamic adjustments of frequency)
* add in phase? (not sure how...)
* when building a signal, structure code so that you can choose the complexity of the data you're representing:
  * a *simple* amplitude is just a scalar value - it's constant for the whole time you're using it.
  * a *dynamic* amplitude is a vector that is the same length as the time vector - it 
* add in error messages to warn user that what they're doing violates certain signal rules:
  * nyquist rate (ie. sample rate is too low).
* add support for both simple signals and IQ version of signal (different representations)
* add support for multiple time units (seconds, miliseconds/microseconds, etc)
* add support for setting time start and stop.
* allow multiple signals to be composed 
  * Signal duration for generation, and then padding at start and stop.
  * All signals must be sampled at the same rate to be composed, or they will not be able to be added together...
* add support to export the data into a certain file format.
* include spectrogram, waterfall plot, and constellation plot