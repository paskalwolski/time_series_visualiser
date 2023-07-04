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
    fig, ax = plt.subplots()

    month_convert = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    df_bar.rename_axis(index=["Year", "Month"], inplace=True)
    df_bar = df_bar.reset_index()
    df_bar = df_bar.pivot(index="Year", columns="Month", values="value")
    df_bar.rename(columns=month_convert, inplace=True)

    # Draw bar plot
    df_bar.plot(ax=ax, kind="bar", xlabel="Years", ylabel="Average Page Views")
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

   # Setting up figure
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(30, 12))
    fig.set_figwidth(20)
    fig.set_figheight(6)

    # Plotting Trend
    sns.boxplot(data=df_box, ax=ax1, x='year', y='value')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title("Year-wise Box Plot (Trend)")
    fig

    # Plotting Seasonality
    sns.boxplot(data=df_box, ax=ax2, x='month', y='value', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    # ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
