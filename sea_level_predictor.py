import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # my method, fails
  # Read data from file

  df = pd.read_csv('epa-sea-level.csv')

  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  # Create scatter plot
  plt.scatter(x, y)

  # Create first line of best fit
  slope, intercept, r, p, se = linregress(x, y)

  x_new = np.arange(1880, 2051, 1)
  y_pred = x_new * slope + intercept

  plt.plot(x_new, y_pred, color="blue")

  # Create second line of best fit
  # subset dataframe
  df_2k = df[df['Year'] >= 2000]

  x_2k = df_2k['Year']
  y_2k = df_2k['CSIRO Adjusted Sea Level']

  slope_2k, intercept_2k, r_2k, p_2k, se_2k = linregress(x_2k, y_2k)

  x_new_2k = np.arange(2000, 2051, 1)
  y_pred_2k = x_new_2k * slope_2k + intercept_2k

  plt.plot(x_new_2k, y_pred_2k, color="orange")

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
