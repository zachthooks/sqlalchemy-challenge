
# Climate Analysis and Flask API

## Overview

This project analyzes historical climate data from Hawaii to provide insights into precipitation, temperature, and weather station data. The analysis is performed using Python, Pandas, SQLAlchemy, and Matplotlib. Additionally, a Flask API is developed to expose key data points and analysis results via user-friendly routes.

---

## Project Structure

- **Jupyter Notebook (`climate_starter.ipynb`)**
  - Performs data analysis and visualization.
  - Connects to a SQLite database (`hawaii.sqlite`) using SQLAlchemy.
  - Includes:
    - Precipitation Analysis: Trends in precipitation over the last year.
    - Station Analysis: Most active weather stations and their temperature observations.

- **Flask App (`app.py`)**
  - Exposes data via an API with the following routes:
    - `/`: Lists all available routes.
    - `/api/v1.0/precipitation`: Provides precipitation data for the last year.
    - `/api/v1.0/stations`: Returns a list of all weather stations.
    - `/api/v1.0/tobs`: Returns temperature observations for the most active station for the last year.
    - `/api/v1.0/<start>`: Returns minimum, average, and maximum temperatures from the specified start date to the end of the dataset.
    - `/api/v1.0/<start>/<end>`: Returns minimum, average, and maximum temperatures for a specified date range.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- SQLite database (`hawaii.sqlite`) in the same directory as the scripts
- Required Python libraries:
  - Flask
  - SQLAlchemy
  - Pandas
  - Matplotlib

Install the dependencies:
```bash
pip install flask sqlalchemy pandas matplotlib
```

---

### Running the Jupyter Notebook
1. Open `climate_starter.ipynb` in Jupyter Notebook or JupyterLab.
2. Execute the cells sequentially to:
   - Analyze precipitation and temperature trends.
   - Visualize the data using Pandas and Matplotlib.

---

### Running the Flask API
1. Open a terminal and navigate to the project directory.
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Access the API by visiting [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

---

## API Routes and Outputs

### `/`
**Description:** Displays all available API routes.

**Example Output:**
```plaintext
Available Routes:
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/<start>
/api/v1.0/<start>/<end>
```

---

### `/api/v1.0/precipitation`
**Description:** Returns the last 12 months of precipitation data in JSON format.

**Example Output:**
```json
{
  "2016-08-23": 0.15,
  "2016-08-24": 0.08,
  ...
}
```

---

### `/api/v1.0/stations`
**Description:** Returns a JSON list of weather stations.

**Example Output:**
```json
[
  {"station": "USC00519397", "name": "WAIKIKI 717.2, HI US"},
  {"station": "USC00519281", "name": "MANOA LYON ARBO 785.2, HI US"},
  ...
]
```

---

### `/api/v1.0/tobs`
**Description:** Returns the last 12 months of temperature observations for the most active station (`USC00519281`).

**Example Output:**
```json
[
  {"date": "2016-08-23", "temperature": 77.0},
  {"date": "2016-08-24", "temperature": 80.0},
  ...
]
```

---

### `/api/v1.0/<start>`
**Description:** Returns the minimum, average, and maximum temperatures for all dates greater than or equal to the start date.

**Example Output:**
```json
[
  {"TMIN": 70.0, "TAVG": 78.3, "TMAX": 85.0}
]
```

---

### `/api/v1.0/<start>/<end>`
**Description:** Returns the minimum, average, and maximum temperatures for dates between the specified start and end dates.

**Example Output:**
```json
[
  {"TMIN": 71.0, "TAVG": 79.2, "TMAX": 86.0}
]
```

---

## Summary

This project provides a demonstration of using Python for data analysis and API development. The Jupyter notebook offers detailed climate data analysis and visualizations, while the Flask API enables access to key results.
