# Parking Lot

Program for parking vehicles in the given available slots with an automated ticketing system

## Problem Statement

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a
number starting at 1 increasing with increasing distance from the entry point in steps of one. We
want to create an automated ticketing system that allows our customers to use our parking lot
without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket
issuing process includes:

1. Taking note of the number written on the vehicle registration plate and the age of the driver of the car.

2. And allocating an available parking slot to the car before actually handing over a ticket to
the driver.

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the
customer returns the ticket which then marks the slot they were using as being available.

The system should provide us with the ability to find out:
1. Vehicle Registration numbers for all cars which are parked by a driver of a certain age
2. Slot number in which a car with a given vehicle registration plate is parked.
3. Slot numbers of all slots where cars of drivers of a particular age are parked.

We interact with the system via a file-based input system i.e. it should accept a filename as an
input. The file referenced by filename will contain a set of commands separated by a newline,
we need to execute the commands in order and produce output.

## Dependencies
You just need Python or Python3 to run this code. Visit the link [https://www.python.org/downloads/](https://www.python.org/downloads/) to download/install Python or follow the instructions below

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