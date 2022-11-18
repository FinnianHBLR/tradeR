import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor

def print_hi():
    nvd = pd.read_csv("./HistoricalData_1668751811642.csv")
    print(nvd.head())
    # Plot share open, high and low.
    plt.plot(nvd.Date, nvd.Open,  color = 'b')
    plt.plot(nvd.Date, nvd.High,  color = 'm')
    plt.plot(nvd.Date, nvd.Low,  color = 'g')

    # Add average
    nvd['Average'] = nvd[['Open', 'High', 'Low']].mean(axis=1)
    plt.plot(nvd.Date, nvd.Average, color='r', linewidth=5, linestyle='dashed')

    # Plot xgboost predicted average price
    X = nvd[['Average']]


    plt.show()

if __name__ == '__main__':
    print_hi()