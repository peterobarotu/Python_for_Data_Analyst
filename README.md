# Solar Energy Forecasting and PV System Modeling

## Project Overview
This project focuses on forecasting solar radiation and modeling energy generation using photovoltaic (PV) systems. The methodology involves predicting **clear sky radiation** using weather variables, followed by predicting **cloudy sky radiation** based on the clear sky radiation and additional meteorological parameters. The study is conducted for **annual forecasting**, as well as separate analyses for the **wet season** and **dry season**.

Finally, the predicted solar radiation is used to model the **actual energy output** of a PV system, incorporating solar panel characteristics and inverter parameters to estimate energy production.

This research was conducted as part of my MSc Energy Economics dissertation at the **Centre for Petroleum, Energy Economics, and Law (CPEEL), University of Ibadan**.

## Methodology
### 1. Predicting Clear Sky Radiation
- Utilized weather variables (temperature, humidity, wind speed, etc.).
- Applied **Machine Learning models** to estimate clear sky solar radiation.

### 2. Predicting Cloudy Sky Radiation
- Used **predicted clear sky radiation** alongside weather variables.
- Developed separate models for **annual, wet season, and dry season** forecasts.

### 3. Model Selection and Validation
- The **Random Forest model** was the best-performing model.
- Used the **Random Forest model** to make predictions on the **validation dataset (year 2022)**.
- The original dataset spans from **2005 to 2022**, with training and test data from **2005 to 2021**.
- Performance metrics were computed by comparing predictions against the actual 2022 data.
- The validated predictions were then used as input for **PVLIB** to model energy generation.

### 4. PV System Energy Modeling
- Converted predicted solar radiation into **actual energy output**.
- Integrated **solar panel specifications** and **inverter efficiency parameters** using PV modeling libraries.

## Data Source
- **Dataset:** Retrieved from the **National Solar Radiation Database (NSRDB)** of **NREL (National Renewable Energy Laboratory).**

## Technologies Used
- **Python** (pandas, NumPy, scikit-learn, TensorFlow, PVLIB)
- **Machine Learning** (Random Forest, LSTM, CNN)
- **Data Visualization** (Matplotlib, Seaborn)
- **Solar Energy Simulation** (PVLIB)

## Repository Structure
```
/solar-energy-forecasting
│── datasets/            # Raw and processed datasets
│── notebooks/           # Jupyter notebooks for analysis and modeling
│── results/             # Model outputs, evaluation reports, and visualizations
│── README.md            # Project description
```

## How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/peterobarotu/Solar_Energy_forecasting.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebooks in the `/notebooks/` directory to reproduce results.

## Author
**Obarotu Peter Urhuerhi**
MSc Energy Economics, CPEEL, University of Ibadan  
LinkedIn: [Your LinkedIn Profile]  
GitHub: [Your GitHub Profile]  



