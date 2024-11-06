import numpy as np
import pandas as pd
data=pd.read_csv('swedish_population_by_year_and_sex_1860-2022.csv', header= 0)
print (data['age']) 

data.describe()