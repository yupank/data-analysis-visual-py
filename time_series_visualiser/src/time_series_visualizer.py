import matplotlib.pyplot as plt
import calendar as cld
import pandas as pd
import seaborn as sns
from datetime import date
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

df = pd.read_csv('fcc-forum-pageviews.csv')
print(df.head())
v_min = df['value'].quantile(0.025)
v_max = df['value'].quantile(0.975)
df = df[(df.value >= v_min) & (df.value <= v_max)]
df_2 = df.copy()

def draw_line_plot():
  # Draw line plot

  #print(df.value.count())
  fig, ax = plt.subplots(figsize=(9, 6))
  sns.lineplot(data=df, x='date', y='value', legend=False, ax=ax)
  #ax.plot(df[id], df.value)
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot

  df_2['year'] = df_2.date.map(lambda str: date.fromisoformat(str).year)
  df_2['month'] = df_2.date.map(lambda str: date.fromisoformat(str).month)
  df_2.date.map(lambda str: date.fromisoformat(str))
  df_2.sort_values(['year', 'month'], ascending=[False, True], inplace=True)

  df_bar = df_2[['date', 'year', 'value']]
  df_bar['month'] = df_2.month.map(lambda m: cld.month_name[m])

  fig, ax = plt.subplots(figsize=(9, 6))

  sns.barplot(data=df_bar,
              x='year',
              y='value',
              hue='month',
              palette='deep',
              ax=ax)

  ax.legend(loc='upper left', title='Months')
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  # Draw bar plot

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  # does not work ! 
  #df_box = df.copy()
  #df_box.reset_index(inplace=True)
  #df_box['year'] = [d.year for d in df_box.date]
  #df_box['month'] = [d.strftime('%b') for d in df_box.date]

  
  df_box = df_2[['date','year','value']]
  df_box['month'] = df_2.month.map(lambda m: cld.month_name[m][:3])
  #print(df_box.head())
  # Draw box plots (using Seaborn)
  fig,(ax1,ax2) = plt.subplots(1,2,figsize =(12,4))
  sns.boxplot(data=df_box,x='year',y='value',ax=ax1)
  sns.boxplot(data=df_box,x='month',y='value',ax=ax2)
  ax1.set_xlabel('Year')
  ax1.set_ylabel('Page Views')
  ax1.set_title ("Year-wise Box Plot (Trend)")
  ax2.set_xlabel('Month')
  ax2.set_ylabel('Page Views')
  ax2.set_title('Month-wise Box Plot (Seasonality)')

  ax1.yaxis.set_major_locator(plt.MultipleLocator(20000))
  ax2.yaxis.set_major_locator(plt.MultipleLocator(20000))

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
