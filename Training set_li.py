# 1. Import training data "1_data_set"
# 2. Data understanding: describe data, clean data
# 3. Split the data set into training and testing subset (k-Fold Cross Validation)
# 4. Select & build the predictive model (i.e Decision tree or regression)
# 5. Test the robustness of the model

import pandas as pd
df=pd.read_csv("C:/Users/dell/Desktop/Munich/04-LMU exchange/05_data science/detective maintainance/1_data_set.csv")
dfd=df.describe()
dfd.to_csv("Data preparation.csv")     # Export the descriptive statistics into a csv file (combined with Svea)x`

print(df.dtypes)                           # Check what data types we have
count_defect=df["defect"].value_counts()
print(count_defect)
clean_up={"defect":{"y":1,"n":0}}
df.replace(clean_up,inplace=True)         # Replace the defact categories into numeric value
df.to_csv("C:/Users/dell/Desktop/Munich/04-LMU exchange/05_data science/detective maintainance/1_data_set_v1.csv",index=False)   

