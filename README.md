# Unit Converter with GUI & History

> A simple Python app to convert Length, Mass and Temperature units, with a Tkinter GUI and saved conversion history.

---

## 📖 Overview
This project provides a user-friendly **Tkinter GUI** to convert units of:
- **Length**: m, km, cm, mm  
- **Mass**: g, kg, mg  
- **Temperature**: C, F, K  

Conversions are saved to a JSON `history` file so users can review recent conversions. The repo also includes automated tests (pytest).

## ✨ Features
- Convert between length, mass and temperature units  
- Tkinter GUI with input fields, category selector, and history panel  
- Conversion history saved to `data/history.json`  
- "Clear history" button in GUI  
- Automated tests for converters and history functions  


## 📁 Folder Structure


## ⚙️ Requirements
- Python **3.10+**
- Tkinter (usually included with Python on macOS/Windows; on Linux you may need to install it)
- pipenv (recommended) or a standard virtualenv


## 🔧 Setup (pipenv — recommended)
1. Install pipenv if needed:
```bash
pip install pipenv
pipenv install pytest tk
pipenv shell

## Run the app
pipenv run python src/gui.py
# or if using venv:
python src/gui.py


## Run the tests
pipenv run pytest tests/


#Features
* Convert Length, Mass, and Temperature units
* Easy-to-use Graphical User Interface (GUI) with Tkinter
* Conversion History stored in history.json
* History display in GUI with option to clear history
* Automated tests for converters and history functions


