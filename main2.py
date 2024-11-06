import numpy as np
import pandas as pd
data=pd.read_csv('swedish_population_by_year_and_sex_1860-2022.csv', header= 0)
print (data['age']) 
data.describe()
#convert the ages (csv) to numeric value
data['age']=pd.to_numeric(data['age'],errors='coerce')
new_df=data.copy()
# age classification
def age_classif(age):
    if age <= 14:
        return 'Children'
    elif 15 <= age <= 64:
        return 'Labor force'
    else:
        return 'Elderly'
# Apply classification to each row
new_df['Category']=data['age'].apply(age_classif)


