# Unit Converter Project

## Overview
This project is a Python Unit Converter with a Tkinter GUI.  
It can convert between **Length, Mass, and Temperature** units.  
The app also keeps a history of conversions using a JSON file.

## Setup
On bash

pip install pipenv
pipenv install pytest tk
pipenv shell

## Run the App
On bash
pipenv run python src/gui.py

## Run Tests
On bash
pytest tests/

## Features
* Convert between Length, Mass, and Temperature
* Save conversion history into a JSON file
* Display history in GUI
* Clear history button
* Automated tests with pytest

## Team Roles
* Conversion Logic Team -> converters
* History Team -> history
* GUI Team -> gui
* Testing Team -> tests
* Media Team -> README and documentation

