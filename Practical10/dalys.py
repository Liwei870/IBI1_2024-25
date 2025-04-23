#import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Change the working directory to the path where the data file is located. Modify it according to the actual situation.
os.chdir("E:\IBI1\IBI1_2024-25\IBI1_2024-25\Practical10")
# Check the current working directory, similar to the pwd command in the Unix command line.
print(os.getcwd())

# List the files in the current directory, similar to the ls command in the Unix command line.
print(os.listdir())

# Read the dataset into a DataFrame.
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# View the first 5 rows of the DataFrame.
print(dalys_data.head(5))

# View the information of the DataFrame, including data types, column names, number of rows, etc.
dalys_data.info()

# Use the describe() function to view the statistical information of numerical columns.
print(dalys_data.describe())

# Display the first 10 rows of data in the third column (Year) of the DataFrame.
year_column_first_10_rows = dalys_data.iloc[0:10, 2]
print(year_column_first_10_rows)
# Note: The 10th year when Afghanistan recorded DALYs data is the last year shown here (determined according to the actual data).

# Use boolean indexing to display the DALYs of all countries in 1990.
is_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[is_1990, 'DALYs']
print(dalys_1990)

# Calculate the average DALYs of the United Kingdom and France.
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"]
france = dalys_data.loc[dalys_data.Entity == "France", "DALYs"]
uk_mean = uk.mean()
france_mean = france.mean()
print(f"Average DALYs in the United Kingdom: {uk_mean}")
print(f"Average DALYs in France: {france_mean}")
# Note: If uk_mean > france_mean, the average DALYs in the United Kingdom are greater than those in France; otherwise, they are less.

# Plot a graph of the change in DALYs over time in the United Kingdom.
uk_data = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.plot(uk_data.Year, uk_data.DALYs, 'b+')
plt.xticks(uk_data.Year, rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Change in DALYs over time in the United Kingdom')
plt.show()

# Answer a custom question: How does the relationship between the DALYs of China and the United Kingdom change over time?
china_uk_data = dalys_data.loc[dalys_data.Entity.isin(["China", "United Kingdom"]), ["Year", "Entity", "DALYs"]]
china_data = china_uk_data.loc[china_uk_data.Entity == "China", ["Year", "DALYs"]]
uk_data = china_uk_data.loc[china_uk_data.Entity == "United Kingdom", ["Year", "DALYs"]]

plt.figure(figsize=(10, 6))
plt.plot(china_data.Year, china_data.DALYs, label='China', marker='o')
plt.plot(uk_data.Year, uk_data.DALYs, label='United Kingdom', marker='s')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Change in DALYs over time in China and the United Kingdom')
plt.legend()
plt.xticks(rotation=-90)
plt.show()
