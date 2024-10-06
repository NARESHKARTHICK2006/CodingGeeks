import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Import the data
df = pd.read_csv('medical_examination.csv')

# Step 2: Add 'overweight' column
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
df = df.drop(columns=['BMI'])

# Step 3: Normalize 'cholesterol' and 'gluc'
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Step 4: Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat = df_cat.rename(columns={'size': 'total'})
    
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar', height=6, aspect=0.75)
    fig = g.fig
    return fig

# Step 5: Clean Data
def clean_data(df):
    df_cleaned = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    return df_cleaned

df_cleaned = clean_data(df)

# Step 6: Draw Heat Map
def draw_heat_map():
    df_heat = clean_data(df)
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', vmax=.3, center=0, square=True, linewidths=0.5, cbar_kws={'shrink': .5}, ax=ax)
    return fig
