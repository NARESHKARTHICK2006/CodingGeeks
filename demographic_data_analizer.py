import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv('census_data.csv')

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100).round(1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0] * 100).round(1)

    # 5. What percentage of people without advanced education make more than 50K?
    no_advanced_education = ~advanced_education
    lower_education_rich = (df[no_advanced_education & (df['salary'] == '>50K')].shape[0] / df[no_advanced_education].shape[0] * 100).round(1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]
    rich_percentage = (rich_min_workers / num_min_workers * 100).round(1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = ((rich_country_counts / country_counts) * 100).idxmax(), (rich_country_counts / country_counts * 100).max().round(1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'
