import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('../medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where(df.weight/((df.height/100)**2) > 25,1,0)
#df['overweight'] = df['height'].map(lambda h: h/2)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.gluc = df.gluc.map(lambda x: 0 if x <=1 else 1)
df.cholesterol = df.cholesterol.map(lambda x: 0 if x <=1 else 1)
print(df.height.count())

# Draw Categorical Plot
def draw_cat_plot():

  df_cat = df.melt(id_vars =['id','cardio'],value_vars = ['active','alco','cholesterol', 'gluc', 'overweight','smoke'])
      # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly. - was not needed
  df_cat.groupby('cardio')
  #print(df_cat.head(4))
  #print(df_cat.tail(4))
  fig=sns.catplot(data=df_cat, x="variable", hue="value", kind="count",col='cardio').fig
  # NOTE: .fig method was said to be deprecated  in Seaborn docs, but .figure did not work
  #print(fig.axes[0].get_ylabel())
  fig.axes[0].set_ylabel('total')
    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    h_lim_min = df['height'].quantile(0.025)
    h_lim_max = df['height'].quantile(0.975)
    w_lim_min = df['weight'].quantile(0.025)
    w_lim_max = df['weight'].quantile(0.975)
    print(f'h: {h_lim_min} -- {h_lim_max}')
    print(f'w: {w_lim_min} -- {w_lim_max}')
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])&(df['height'] >= h_lim_min)&(df['height'] <= h_lim_max)&(df['weight']>= w_lim_min )&(df['weight'] <= w_lim_max)]
    #df_heat = df[(df['ap_lo'] <= df['ap_hi'])&&(df['height'] >= df['height'].quantile(0.025))]
    #print(df_heat.head())
    #print(df_heat.tail())
    print(df_heat.height.count())
    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9,8))
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', vmin = -0.1, vmax = 0.3, linewidth=.5,square=True, ax=ax)



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
