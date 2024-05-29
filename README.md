# <span style="font-width:bold; font-size: 3rem; color:#2656a3;">**Msc. BDS - M7 Second Semester Project** 
EXAM ASSIGNMENT - Repository for semester project.

## Expectations and Format for the Semester Project:
The semester project represents the first significant milestone in applying the knowledge and skills acquired from the curriculum. It's designed to bridge the gap between theoretical understanding and real-world application.

Format should include:
- Functional ML pipeline suited for the project.
- One or multiple GitHub repositories demonstrating the code for each segment in the pipeline.
- Project report. The report is a (semi/non) technical documentation.
- Topic can be any real-world problem. 
- A functional frontend application.

## Objectives:
This repository contains all notebooks and local data files for the final second-semester project on the Master in Business Data Science at Aalborg University Business School.

This project aims to build a prediction system that forecasts the electricity prices in Denmark (area DK1) based on weather conditions, previous prices, and the Danish calendar.

## Structure:
There are six notebooks in the folder "*pipeline*":

1. **Feature Backfill**: Historical data is loaded and we engineer and create feature groups in Hopswork. Moving Window is applied as a feature engineering technique trying to smooth out short-term fluctuations and highlight longer-term trends or cycles in the time-series data. Exploratory Data Analysis is performed aimed at understanding the characteristics and underlying patterns within the data.
2. **Feature Pipeline**: New data are parsed and inserted into the feature groups.
3. **Training Pipeline XGBRegressor**: Building feature view, training dataset split, training the model and evaluating, and saving it in the Model Registry.
4. **Training Pipeline LSTM**: Building feature view, model architecture, and training dataset split, training the model, and saving it in the Model Registry.
5. **Inference Pipeline XGBRegressor**: Loading new forecasted weather measures for final predictions. The trained model is retrieved from the model registry and used for inference and electricity price predictions on the new data.
6. **Inference Pipeline LSTM**: Loading new forecasted weather measures for final predictions. The trained model is retrieved from the model registry and used for inference and electricity price predictions on the new data.

The structure of the notebooks is largely inspired by [Hopsworks tutorials](https://github.com/logicalclocks/hopsworks-tutorials).
Inspiration for code snippets has been taken from the following advanced tutorials [air_quality](https://github.com/logicalclocks/hopsworks-tutorials/tree/master/advanced_tutorials/air_quality), [electricity](https://github.com/logicalclocks/hopsworks-tutorials/tree/master/advanced_tutorials/electricity), and [timeseries](https://github.com/logicalclocks/hopsworks-tutorials/tree/master/advanced_tutorials/timeseries).

[Hopsworks](https://www.hopsworks.ai) is used as the platform to store features in the **Hopworks Feature Store** and save the trained models in **Hopworks Model Registry**. Daily instance generation is done through GitHub Actions where the Feature pipeline and both inference pipelines are scheduled to run at 01:55 UTC everyday.

## Data Pipeline:
The overall architecture of the Electricity Pipeline is illustrated below. Inspiration is taken from [Lecture 1 - serverless ml course feature pipelines](https://drive.google.com/file/d/1L8DHGC5xo0NlNe8xfh4xf4NZV1CEGBA6/view). 

![electricity_pipeline.png](images/electricity_pipeline.png)

## Data:
The data used comes from the following sources:

- Hourly electricity prices in Denmark per day from [Energinet/Energidataservice](https://www.energidataservice.dk).
- Different meteorological observations based on Aalborg Denmark from [Open Meteo](https://www.open-meteo.com).
- Weather Forecast based on Aalborg Denmark also from [Open Meteo](https://www.open-meteo.com).
- Danish calendar that categorizes dates into types based on whether it is a workday or not. The Calendar is imported from the Python Danish holidays library.

See corresponding functions in the folder [features](https://github.com/tobiasmj97/bds_m7_second-semester-project/tree/main/features). The functions include the initial API call and the following data preprocessing.

## Model Performance Comparison:
We initialize XGBoost Regressor and Long-Short-Term Memory as the models used for training, separated into separate pipelines. 
The models are fitted to the train data and further evaluated on test sets using validation metric functions from the sklearn library. A snapshot of the last 5 predicted prices and their corresponding actual prices are displayed for translating the models' performances from technical to non-technical audiences. 

### XGB Regressor 
| Validation metrics   | Value    |  
|----------------------|----------|
| MSE                  | 0.046    |
| MAE                  | 0.161    |
| RMSE                 | 0.214    |

| Predicted Prices   | Actual Prices  |  
|--------------------|----------------|
| 1: 0.360993        | 1: 0.66118     |
| 2: 0.361774        | 2: 0.62298     |
| 3: 0.368297        | 3: 0.53649     |
| 4: 0.324221        | 4: 0.09887     |
| 5: 0.301910        | 5: 0.00015     |

### LSTM
| Validation metrics   | Value    |  
|----------------------|----------|
| Loss                 | 0.005    |
| MSE                  | 0.455    |
| MAE                  | 0.531    |
| RMSE                 | 0.674    |

| Predicted Prices   | Actual Prices  |  
|--------------------|----------------|
| 1: 0.789154        | 1: 0.88047     |
| 2: 0.717946        | 2: 0.73004     |
| 3: 0.636073        | 3: 0.56447     |
| 4: 0.538946        | 4: 0.55880     |
| 5: 0.440306        | 5: 0.47829     |

## Frontend Application on 🤗 Hugging Face Spaces:
We have made a functional frontend application that visually demonstrates the project’s application in real-world scenarios. The Streamlit application is located in the following [Github Repository](https://github.com/tobiasmj97/bds_m7_second-semester-project_streamlit).

Streamlit app is hosted on [Huggingface](https://huggingface.co/spaces/tobiasmj97/sp_forecast_electricity_prices).

