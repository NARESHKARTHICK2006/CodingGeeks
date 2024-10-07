import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    
    df = pd.read_csv('epa-sea-level.csv')

    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_extended, color='red', label='Best Fit Line (1880-2050)')

    
    recent_df = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, r_value, p_value, std_err = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])

    
    recent_years_extended = pd.Series(range(2000, 2051))
    recent_sea_levels_extended = recent_intercept + recent_slope * recent_years_extended
    plt.plot(recent_years_extended, recent_sea_levels_extended, color='green', label='Best Fit Line (2000-2050)')

    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
