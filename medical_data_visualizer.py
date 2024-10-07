import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('medical_examination.csv')


df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
df = df.drop(columns=['BMI'])


df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat = df_cat.rename(columns={'size': 'total'})
    
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar', height=6, aspect=0.75)
    fig = g.fig
    return fig


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


def draw_heat_map():
    df_heat = clean_data(df)
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', vmax=.3, center=0, square=True, linewidths=0.5, cbar_kws={'shrink': .5}, ax=ax)
    return fig
