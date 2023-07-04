import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')
# Clean data
bottom_percentile = df['value'].quantile(0.025)
top_percentile = df['value'].quantile(0.975)
df = df[df['value'] >= bottom_percentile]
df = df[df['value'] <= top_percentile]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots()
    df.plot(ax=ax, title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Visits", legend=False, figsize=(12, 4), color="red")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # average daily page views for each month grouped by year.
    # The legend should show month labels and have a title of Months. 
    # On the chart, the label on the x axis should be Years and 
    # the label on the y axis should be Average Page Views.
   
    fig, ax = plt.subplots()
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    print(df_bar.head())
    df_bar = df_bar.reset_index()
    df_bar.plot(ax=ax, kind="bar")
    
    # Draw bar plot

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
