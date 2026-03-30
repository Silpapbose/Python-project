
## **Weather Analyzer**

A Python-based command-line tool to analyze weather data from a CSV dataset.
This project demonstrates Python packaging, data analysis, and visualization using real-world weather data.

---

## Author

**Silpa Bose**

---

## Project Overview

This project reads weather data from a CSV file and provides useful insights such as:

* Average, minimum, and maximum temperature
* Temperature trends over time
* Visualization of temperature changes

It is implemented as a **Python package** and can be executed via the command line.

---

##  Features

*  Load weather dataset from CSV
*  Compute temperature statistics (avg, min, max)
*  Detect temperature trends (increasing/decreasing)
*  Generate and save temperature graph
*  CLI support with arguments (`--file`, `--column`)
*  Installable Python package using `pyproject.toml`

---

##  Technologies Used

* Python 3.10+
* pandas
* matplotlib

---

##  Project Structure

```
weather-analyzer/
│
├── pyproject.toml
├── README.md
│
├── data/
│   └── weather.csv
│
├── weather_analyzer/
│   ├── __init__.py
│   ├── __main__.py
│   ├── loader.py
│   └── analysis.py
```

---

## Installation

Clone the repository:

```bash
git https://github.com/Silpapbose/Python-project
cd Python-project
```

Install the package:

```bash
pip install -e .
```

or

uv venv
source .venv/bin/activate
uv pip install -e .
uv run -m weather_analyzer

---

##  Usage

### Run with default dataset:

```bash
python -m weather_analyzer
```

### Specify custom dataset:

python -m weather_analyzer --file data/weather.csv

### Specify column:

python -m weather_analyzer --column "Temperature (C)"


### Full example:

python -m weather_analyzer --file data/weather.csv --column "Temperature (C)"

---

##  Output

The tool provides:

* Temperature statistics (average, min, max)
* Trend analysis
* A saved graph

---

##  Dataset

The dataset used is a weather dataset containing:

* Temperature
* Humidity
* Wind speed
* Pressure
* Date and time

Place the dataset inside: data/weather.csv


---

##  Notes

* The project uses a local CSV dataset (no API dependency)
* Graph is saved as an image instead of opening a GUI window
* Timezone issues are handled during datetime parsing

---



