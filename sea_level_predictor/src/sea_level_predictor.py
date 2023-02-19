import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('./epa-sea-level.csv')
  df_2000 = df[df['Year']>=2000]
  #print(df_2000.head())
  y_name = 'CSIRO Adjusted Sea Level'
  res = linregress(df['Year'],df[y_name])
  res_2000 = linregress(df_2000['Year'],df_2000[y_name])
  #print(res.slope,res.intercept)
  t1 = np.linspace(1880,2050,num=171)
  t2 = np.linspace(2000,2050,num=51)
  print(t2[0],t1[133])
  plt.plot(df['Year'],df[y_name],'go',label = 'CSIRO data')
  plt.plot(t1, res.intercept + res.slope*t1, 'r', label='fitted all data')
  plt.plot(t2, res_2000.intercept + res_2000.slope*t2, 'b--', label='fit data since 2000')
  plt.legend()
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  plt.show()