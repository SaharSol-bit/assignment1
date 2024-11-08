import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
data = pd.read_csv('swedish_population_by_year_and_sex_1860-2022.csv', header= 0)

data.describe()

#convert the string values from the csv to numeric value
data['age'] = pd.to_numeric(data['age'],errors='coerce')

#convert year columns to numeric values
for year in range(1860,2023):
    string = str(year)
    data[string]=pd.to_numeric(data[string],errors='coerce')
#make a new dataframe
new_df = data.copy()
#function for age classification
def age_classif(age):
    if age <= 14:
        return 'Children'
    elif 15 <= age <= 64:
        return 'Labor force'
    else:
        return 'Elderly'
# Apply classification to each row
new_df['Category']=data['age'].apply(age_classif)

# Sum population
df_2 = new_df.groupby(['Category']).sum(numeric_only=True) #sum all the values from each category per year
df_2 = df_2.drop(columns=['age']) #delete age column


# function to calculate dependency ratio
def depend_ratio(children,elder,lab_force):
    return ((children+elder)/lab_force)*100 if lab_force != 0 else np.nan
    
#create an array with the dependency ratios
dependency_ratios = []
for i in range(1860,2023):
    # we use append in order to add the value to the list
    year_string = str(i)
    children = df_2.loc['Children', year_string]
    elderly = df_2.loc['Elderly',year_string]
    labor_force = df_2.loc['Labor force', year_string]
    dependency_ratios.append(depend_ratio(children,elderly,labor_force))
#convert list into array
dependency_ratios=np.array(dependency_ratios)
print(dependency_ratios)

# Create the plot
years = np.arange(1860, 2023)
plt.figure(figsize=(12, 6))
plt.plot(years, dependency_ratios)
plt.title("Sweden's Dependency Ratio (1860-2022)")
plt.xlabel('Year')
plt.ylabel('Dependency Ratio')
plt.grid(True)
plt.show()

#calculate fraction
children_fraction = []
elderly_fraction = []
dependent_fraction = []

for i in range(1860,2023):
    year_string = str(i)
    children = df_2.loc['Children', year_string]
    elderly = df_2.loc['Elderly', year_string]
    labor_force = df_2.loc['Labor force', year_string]
    total_population = children + elderly + labor_force
    
    children_fraction.append((children / total_population)*100)
    elderly_fraction.append((elderly / total_population)*100)
    dependent_fraction.append(((children + elderly) / total_population)*100)

# Plot population fractions
plt.figure(figsize=(12, 6))
plt.plot(years, children_fraction, label='Children (0-14)', color = 'red')
plt.plot(years, elderly_fraction, label='Elderly (65+)', color = 'blue')
plt.plot(years, dependent_fraction, label='Total Dependent', color = 'green')
plt.title('Population Fractions in Sweden (1860-2022)')
plt.xlabel('Year')
plt.ylabel('Percentage of Total Population')
plt.grid(True)
plt.show()
