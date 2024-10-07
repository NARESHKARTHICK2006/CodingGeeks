import pandas as pd

def demographic_data_analyzer():
    
    df = pd.read_csv('census_data.csv')

    
    race_count = df['race'].value_counts()

    
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100).round(1)

    
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0] * 100).round(1)


    no_advanced_education = ~advanced_education
    lower_education_rich = (df[no_advanced_education & (df['salary'] == '>50K')].shape[0] / df[no_advanced_education].shape[0] * 100).round(1)

    
    min_work_hours = df['hours-per-week'].min()

    
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]
    rich_percentage = (rich_min_workers / num_min_workers * 100).round(1)


    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = ((rich_country_counts / country_counts) * 100).idxmax(), (rich_country_counts / country_counts * 100).max().round(1)

    
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'
