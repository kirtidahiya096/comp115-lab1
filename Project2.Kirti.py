import pandas as pd                                                                                   # importing pandas which is a library used for data analysis. it will help me to read file and manipulate data in a tabular format. 

df = pd.read_csv("BC Census 2016 data.csv")                                                           # this will read the csv file and store it in variable df as dataframe. df is structure with rows and columns. 

# TASK 1 
print("TASK 1 RESULTS: \n")                                                                           # Just printing the title 

high_rent = df[df['shelt_rent_30plus_rate'] > 50]                                                     # here we are filtering to get only those rows where the shelter rent burden is greater than 50%.

print("Areas where renters spend more than 50% of their income on shelter : \n")
print(high_rent[['chsa', 'shelt_rent_30plus_rate', 'median_household_income', 'median_rent']])

# TASK 2 
print("\nTASK 2 RESULTS: \n")

pha_group = df.groupby('pha')['shelt_rent_30plus_rate'].mean()                                        # here we are grouping the data by pha and calculating the average shelter rent burden for each group. we are using mean fucntion to calculate the average. 

print("Average shelter rent burden for each Public Health Area (PHA) : \n")
print(pha_group)

# TASK 3 

import matplotlib.pyplot as plt                                                                       # used for creating bar chart to visualize the average shelter rent burden for each pha. 

pha_group.plot(kind='bar', color = 'skyblue')                                                         # this will create a bar chart with average shelter rent burden for each pha. i am using skyblue color for the bars. 
plt.title('Average Shelter Rent Burden by Public Health Area (PHA)')
plt.xlabel('Public Health Area (PHA)')
plt.ylabel('Average Shelter Rent Burden (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()                                                                                            # this will display the bar chart. 
