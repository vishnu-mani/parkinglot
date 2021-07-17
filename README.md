# Parking Lot

Program for parking vehicles in the given available slots with an automated ticketing system

## Installation
Installing Python 3 on Linux
```bash
sudo apt-get update
sudo apt-get install python3.8
sudo apt-get install python3-pip
```
Installing Python 3 on Mac

To [install Homebrew](https://brew.sh/), open Terminal and run
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
Now, we can install Python 3:
```bash
brew install python
```
Then, the `pip` or `pip3` is installed automatically & if not please run the following commands
```bash
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```
## Execution

For executing the program for Parking Lot

```bash
python ParkingLot.py
```

## Run Unit Test

For testing the program code with unit test cases

```bash
python TestParkingLot.py
```

## Code Coverage

The amount lines/blocks of your code are executed while the automated tests are running.

#### Installation

```bash
pip3 install coverage
```

For running code coverage for unit tests
```bash
coverage run TestParkingLot.py
```
For running code coverage for program with input `test_input.txt`
```bash
coverage run ParkingLot.py
```
For getting the code coverage report

```bash
coverage report -m
```
