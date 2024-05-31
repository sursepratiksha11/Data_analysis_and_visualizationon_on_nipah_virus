import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def generate_graph():
    # Read data from Excel file
    def read_data_from_excel(file_path):
        df = pd.read_excel(file_path)
        years = df['Year'].values
        cases = df['Cases_India'].values
        return years, cases

    # File path containing the historical data in Excel format
    file_path = 'C:/Users/Dell/Desktop/Projects 2 yr/PBL-Project/PBL-Project/casesData.xlsx'

    # Read data from Excel file
    yearsForIndia, casesForIndia = read_data_from_excel(file_path)

    # Fit linear regression model
    model = LinearRegression()
    model.fit(yearsForIndia.reshape(-1, 1), casesForIndia)

    # Years for prediction
    years_to_predict = np.arange(2025, 2035, 2).reshape(-1, 1)
    predicted_cases = model.predict(years_to_predict)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plotting the historical data
    plt.plot(yearsForIndia, casesForIndia, color='blue', marker='o', label='Historical Data')

    # Plotting the predicted data
    plt.plot(years_to_predict, predicted_cases, color='red', linestyle='-', marker='o', label='Predicted Data')

    # Displaying predicted cases for each year
    for year, cases in zip(years_to_predict.flatten(), predicted_cases):
        plt.text(year, cases, f'{cases:.0f}', ha='center', va='bottom', color='red')

    # Setting x-axis and y-axis ranges
    plt.xlim(min(yearsForIndia[0], years_to_predict[0]), max(years_to_predict[-1]))
    plt.ylim(0, max(max(casesForIndia), max(predicted_cases)) + 5)

    # Adding labels and title
    plt.title('Nipah Virus Cases in India')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Return the x and y data for plotting
    return yearsForIndia, casesForIndia

# Uncomment the below line to test the generate_graph function independently
generate_graph()
