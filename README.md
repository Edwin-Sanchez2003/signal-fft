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