import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('swedish_population_by_year_and_sex_1860-2022.csv', header= 0)
print(data['age'])
data.describe()
#convert the string values from the csv to numeric value
data['age'] = pd.to_numeric(data['age'],errors='coerce')
for i in range(1860,2023):
    string = str(i)
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
print(df_2)

#df_2.to_csv('categories_per_year2.csv',index=True)
categories = pd.read_csv('categories_per_year2.csv', header= 0)

# function to calculate dependency ratio
def depend_ratio(children,elder,lab_force):
    DR = ((children+elder)/lab_force)*100
    return DR
#create an array with the dependency ratios
dependency_ratios = []
for i in range(1860,2023):
    # we use append in order to add the value to the list
    string = str(i)
    dependency_ratios.append(depend_ratio(categories[string][0],categories[string][1],categories[string][2]))
#convert list into array
dependency_ratios=np.array(dependency_ratios)
print(dependency_ratios)

# array of years
years=[]
for k in range(1860,2023):
   years.append(k)
#convert list to array
years=np.array(years)
print(years)


# Plot dependency ratios
fig, ax = plt.subplots() #Create a figure containing single axes
ax.plot(years,dependency_ratios)
ax.set_xlabel('years')
ax.set_ylabel('dependency ratio')
ax.set_title('Dependency ratio in Sweden')
plt.show()







