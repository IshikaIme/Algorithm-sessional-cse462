#regression 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def log_array(arr):
    return np.array([np.log10(e) for e in arr])  # Use np.log10 for base-10 logarithm

def get_regression_line_coefficients(x, y):
    return np.polyfit(log_array(x), log_array(y), 1)

def plot_regression_data(file_path, label):
    data = pd.read_csv(file_path, sep=',')
    n = data['n'].values
    waste = data['waste'].values

    m, b = get_regression_line_coefficients(n, waste)

    # Plot original data points
    plt.plot(n, waste, 'o', label=f'{label} data')

    # Plot regression line
    x_regression = np.logspace(np.log10(n.min()), np.log10(n.max()), 100)  # Generate smooth line
    y_regression = m * log_array(x_regression) + b
    plt.plot(x_regression, 10**y_regression, label=f'{label} regression: y ~ {round(m, 3)}x + {round(b, 3)}')

def main():
    file_list = [
       r"E:\BUET CSE  18\4-2\algo\ime\data\first_fit.csv",
 r"E:\BUET CSE  18\4-2\algo\ime\data\best_fit_decreasing.csv"
        
    ]

    plt.figure(figsize=(10, 6))  # Adjust figure size for better visualization

    for fname in file_list:
        filename = fname.split("\\")[-1]
        plot_regression_data(fname, filename.rstrip(".csv"))

    plt.xlabel("n")
    plt.ylabel("Waste")
    plt.title("Regression Analysis of two first-fit and best-fit-decreasing Algorithms")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
