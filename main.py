import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def g1():
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

    # Return the plot
    return plt


def g2():
    def read_data_from_excel(file_path):
        df = pd.read_excel(file_path)
        years = df['Year'].values
        cases = df['Cases_Malaysia'].values
        return years, cases

    file_path = 'C:/Users/Dell/Desktop/Projects 2 yr/PBL-Project/PBL-Project/casesData.xlsx'

    yearsForMalaysia, casesForMalaysia = read_data_from_excel(file_path)

    model = LinearRegression()
    model.fit(yearsForMalaysia.reshape(-1, 1), casesForMalaysia)

    years_to_predict = np.arange(2025, 2040, 1).reshape(-1, 1)
    predicted_cases = model.predict(years_to_predict)

    plt.figure(figsize=(10, 6))

    plt.plot(yearsForMalaysia, casesForMalaysia, color='blue', marker='o', label='Historical Data')

    plt.plot(years_to_predict, predicted_cases, color='red', linestyle='-', marker='o', label='Predicted Data')

    for year, cases in zip(years_to_predict.flatten(), predicted_cases):
        plt.text(year, cases, f'{cases:.0f}', ha='center', va='bottom', color='red')

    plt.title('Nipah Virus Cases in Malaysia')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid(True)

    return plt


def g3():
    def read_data_from_excel(file_path):
        df = pd.read_excel(file_path)
        years = df['Year'].values
        cases = df['Cases_Bangladesh'].values
        return years, cases

    file_path = 'C:/Users/Dell/Desktop/Projects 2 yr/PBL-Project/PBL-Project/casesData.xlsx'

    yearsForBangladesh, casesForBangladesh = read_data_from_excel(file_path)

    model = LinearRegression()
    model.fit(yearsForBangladesh.reshape(-1, 1), casesForBangladesh)

    years_to_predict = np.arange(2025, 2035, 2).reshape(-1, 1)
    predicted_cases = model.predict(years_to_predict)

    plt.figure(figsize=(10, 6))

    plt.plot(yearsForBangladesh, casesForBangladesh, color='blue', marker='o', label='Historical Data')

    plt.plot(years_to_predict, predicted_cases, color='red', linestyle='-', marker='o', label='Predicted Data')

    for year, cases in zip(years_to_predict.flatten(), predicted_cases):
        plt.text(year, cases, f'{cases:.0f}', ha='center', va='bottom', color='red')

    plt.xlim(min(yearsForBangladesh[0], years_to_predict[0]), max(years_to_predict[-1]))
    plt.ylim(0, max(max(casesForBangladesh), max(predicted_cases)) + 5)

    plt.title('Nipah Virus Cases in Bangladesh')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid(True)
    plt.show()
    return plt


def g4():
    states = ['Kerala', 'West Bengal', 'Perak', 'Negeri Sembilan', 'Selangor', 'Pahang', 'Kuala Lumpur', 'Sarawak',
              'Faridpur', 'Tangail', 'Rajbari', 'Kushtia', 'Jhalokati', 'Naogaon', 'Manikganj', 'Gopalganj',
              'Mymensingh', 'Joypurhat', 'Chandpur', 'Khulna', 'Magura', 'Satkhira', 'Rangpur', 'Yunnan', 'Hunnan']
    species = ['Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis',
               'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis', 'Cynopterus brachyotis',
               'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb',
               'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb',
               'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb', 'Pteropus mediusb',
               'Megaderma lyra', 'Hipposideros larvatus', 'Cynopterus sphinx']

    state_species = {
        'Kerala': ['Cynopterus brachyotis', 'Taphozous melanopogon', 'Cynopterus sphinx', 'Megaderma lyra'],
        'West Bengal': ['Cynopterus brachyotis', 'Cynopterus sphinx'],
        'Perak': ['Cynopterus brachyotis', 'Megaerops ecaudatus', 'Hipposideros larvatus', 'Eonycteris spelaea'],
        'Negeri Sembilan': ['Cynopterus brachyotis'],
        'Selangor': ['Cynopterus brachyotis'],
        'Pahang': ['Cynopterus brachyotis'],
        'Kuala Lumpur': ['Cynopterus brachyotis'],
        'Sarawak': ['Cynopterus brachyotis'],
        'Faridpur': ['Pteropus mediusb', 'Hipposideros larvatus'],
        'Tangail': ['Pteropus mediusb'],
        'Rajbari': ['Pteropus mediusb'],
        'Kushtia': ['Pteropus mediusb'],
        'Jhalokati': ['Pteropus mediusb'],
        'Naogaon': ['Pteropus mediusb'],
        'Manikganj': ['Pteropus mediusb'],
        'Gopalganj': ['Pteropus mediusb'],
        'Mymensingh': ['Pteropus mediusb'],
        'Joypurhat': ['Pteropus mediusb'],
        'Chandpur': ['Pteropus mediusb', 'Hipposideros larvatus'],
        'Khulna': ['Pteropus mediusb'],
        'Magura': ['Pteropus mediusb'],
        'Satkhira': ['Pteropus mediusb'],
        'Rangpur': ['Pteropus mediusb'],
        'Yunnan': ['Megaderma lyra', 'Hipposideros larvatus', 'Cynopterus sphinx'],
        'Hunnan': ['Megaderma lyra', 'Hipposideros larvatus', 'Cynopterus sphinx']
    }

    state_countries = {
        'Kerala': 'India',
        'West Bengal': 'India',
        'Perak': 'Malaysia',
        'Negeri Sembilan': 'Malaysia',
        'Selangor': 'Malaysia',
        'Pahang': 'Malaysia',
        'Kuala Lumpur': 'Malaysia',
        'Sarawak': 'Malaysia',
        'Faridpur': 'Bangladesh',
        'Tangail': 'Bangladesh',
        'Rajbari': 'Bangladesh',
        'Kushtia': 'Bangladesh',
        'Jhalokati': 'Bangladesh',
        'Naogaon': 'Bangladesh',
        'Manikganj': 'Bangladesh',
        'Gopalganj': 'Bangladesh',
        'Mymensingh': 'Bangladesh',
        'Joypurhat': 'Bangladesh',
        'Chandpur': 'Bangladesh',
        'Khulna': 'Bangladesh',
        'Magura': 'Bangladesh',
        'Satkhira': 'Bangladesh',
        'Rangpur': 'Bangladesh',
        'Yunnan': 'China',
        'Hunnan': 'China'
    }

    plt.figure(figsize=(12, 6))
    for state, species_list in state_species.items():
        y_values = [states.index(state) + 1] * len(species_list)
        plt.scatter(species_list, y_values, color='skyblue', marker='o')

    yticks_labels = [f"{state} ({state_countries[state]})" for state in states]
    plt.yticks(range(1, len(states) + 1), yticks_labels)

    plt.title('Bat Species Distribution Across States')
    plt.xlabel('Bat Species')
    plt.ylabel('State (Country)')
    plt.grid(True)

    return plt


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Combined Graphs")
        self.geometry("800x600")

        style = ttk.Style()
        style.theme_create("custom", parent="alt", settings={
            "TNotebook.Tab": {
                "configure": {"padding": [10, 5], "font": ('TkDefaultFont', 12)},
                "map": {"background": [("selected", "lightblue")],
                        "foreground": [("selected", "black")]}
            }
        })
        style.theme_use("custom")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.frames = {}
        self.files = ["file1.py", "file2.py", "file3.py", "file4.py"]
        for idx, title in enumerate(["Graph 1", "Graph 2", "Graph 3", "Graph 4"]):
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=title)
            self.frames[idx] = frame

        self.notebook.bind("<<NotebookTabChanged>>", self.handle_tab_change)

    def handle_tab_change(self, event):
        idx = self.notebook.index(self.notebook.select())

        frame = self.frames[idx]
        for widget in frame.winfo_children():
            widget.destroy()

        self.execute_file(idx)

    def execute_file(self, idx):
        if idx == 0:
            plt = g1()
        elif idx == 1:
            plt = g2()
        elif idx == 2:
            plt = g3()
        elif idx == 3:
            plt = g4()
        else:
            exit(0)

        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.frames[idx])
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
