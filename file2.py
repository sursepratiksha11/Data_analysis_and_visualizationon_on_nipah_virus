import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

def generate_graph():
    # Read data from Excel file
    def read_data_from_excel(file_path):
        df = pd.read_excel(file_path)
        years = df['Year'].values
        cases = df['Cases_Malaysia'].values
        return years, cases

    # File path containing the historical data in Excel format
    file_path = "C:/Users/Dell/Desktop/Projects 2 yr/PBL-Project/PBL-Project/casesData.xlsx"

    # Read data from Excel file
    yearsForMalaysia, casesForMalaysia = read_data_from_excel(file_path)

    # Fit linear regression model
    model = LinearRegression()
    model.fit(yearsForMalaysia.reshape(-1, 1), casesForMalaysia)

    # Years for prediction
    years_to_predict = np.arange(2025, 2040, 1).reshape(-1, 1)
    predicted_cases = model.predict(years_to_predict)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plotting the historical data
    plt.plot(yearsForMalaysia, casesForMalaysia, color='blue', marker='o', label='Historical Data')

    # Plotting the predicted data
    plt.plot(years_to_predict, predicted_cases, color='red', linestyle='-', marker='o', label='Predicted Data')

    # Displaying predicted cases for each year
    for year, cases in zip(years_to_predict.flatten(), predicted_cases):
        plt.text(year, cases, f'{cases:.0f}', ha='center', va='bottom', color='red')

    # Adding labels and title
    plt.title('Nipah Virus Cases in Malaysia')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid(True)
    plt.show()
    # Return the x and y data for plotting
    return yearsForMalaysia, casesForMalaysia

# Uncomment the below line to test the generate_graph function independently
generate_graph()
