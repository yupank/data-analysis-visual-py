import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  dataFrame = pd.read_csv('adult.data.csv')
  print(dataFrame.head(3))
  #for i in range(15):
  #print(dataFrame.columns[i])

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  #race_count = list();
  race_count = dataFrame['race'].value_counts()
  #for count in race_list:
  #race_count.append(count)

  # What is the average age of men?
  men = dataFrame[dataFrame['sex'] == 'Male']
  average_age_men = round(men['age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?

  BSc = dataFrame[dataFrame['education'] == 'Bachelors']
  percentage_bachelors = round(
    100 * len(BSc['education']) / len(dataFrame['education']), 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  hEd = dataFrame[(dataFrame['education'] == 'Bachelors') |
                  (dataFrame['education'] == 'Masters') |
                  (dataFrame['education'] == 'Doctorate')]
  
  lEd = dataFrame[(dataFrame['education-num'] < 13)
                  | (dataFrame['education'] == 'Prof-school')]

  higher_education = len(hEd['education'])
  lower_education = len(lEd['education'])
  #  print(higher_education / (higher_education + lower_education))
  hEd_rich = hEd[hEd['salary'] == '>50K']
  lEd_rich = lEd[lEd['salary'] == '>50K']

  # percentage with salary >50K
  higher_education_rich = round(
    100 * len(hEd_rich['education']) / higher_education, 1)
  lower_education_rich = round(
    100 * len(lEd_rich['education']) / lower_education, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = dataFrame['hours-per-week'].min()
  minWorkers = dataFrame[(dataFrame['hours-per-week'] == min_work_hours)]

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = len(minWorkers['hours-per-week'])
  min_workers_rich = minWorkers[minWorkers['salary'] == '>50K']
  rich_percentage = round(100*len(min_workers_rich['hours-per-week']) / num_min_workers, 1)

  # What country has the highest percentage of people that earn >50K?
  hEarners = dataFrame[dataFrame['salary']=='>50K']
  h_country_count = hEarners['native-country'].value_counts()
  
  ratioByCountry = h_country_count.sort_index()
  #print(ratioByCountry)
  lEarners = dataFrame[dataFrame['salary']=='<=50K']
  l_country_count = lEarners['native-country'].value_counts()
  l_country_count.sort_index(inplace = True)

  for idx in ratioByCountry.index:
    ratioByCountry.loc[idx]=round(
      100*ratioByCountry.loc[idx]/(ratioByCountry.loc[idx]+l_country_count.loc[idx]),1)
    #print(f'{idx}: {ratioByCountry.loc[idx]}')
  ratioByCountry.sort_values(ascending = False, inplace = True)
  #print(ratioByCountry)
  highest_earning_country = ratioByCountry.index[0]
  highest_earning_country_percentage = ratioByCountry.iat[0]

  # Identify the most popular occupation for those who earn >50K in India.
  hE_Ind = dataFrame[(dataFrame['native-country'] == 'India')
                  & (dataFrame['salary'] == '>50K')]
  hE_Ind_count = hE_Ind['occupation'].value_counts()

  top_IN_occupation = hE_Ind_count.index[0]

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
