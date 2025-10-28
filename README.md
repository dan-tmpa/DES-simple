# Monte Carlo + Discrete-Event Simulation: a simple case
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)

This repository contains a simple example of a Discrete-Event Simulation (DES) as the underlying structure for Monte Carlo estimation of random quantities. 
The DES features the failure and repair dynamics of a single component. The time to failure follows a Weibull probability distribution with shape parameter = 1.5 and scale parameter = 2000 h. The time to repair follows an exponential distribution with rate parameter (or repair rate) of 4E-03 1/h. The mission time is equal to 5 years. The results are generated for 1,000, 10,000 and 100,000 simulation runs.

## Usage

1. Have Python 3.11 or later installed.
2. Clone this repository:
```
git clone https://github.com/dan-tmpa/DES-simple
```
3. Inside the created folder, install dependencies:
```
pip install -r requirements.txt
```
4. Run the Python script.
```
python des.py
```