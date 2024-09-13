# import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read csv file
data_set = pd.read_csv(
    "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
)

data = data_set[
    (data_set["STUB_NAME"] == "Total")
    & (data_set["AGE"] == "All ages")
    & (data_set["PANEL"] == "All drug overdose deaths")
    & (data_set["UNIT"] == "Deaths per 100,000 resident population, crude")
]

# calculating mean, median and mode
mean = data["ESTIMATE"].mean()
median = data["ESTIMATE"].median()
std = data["ESTIMATE"].std()
print(f"This is the mean is {mean}")
print(f"This is the median is {median}")
print(f"This is the standard deviation is {std}")

# Create visualization
plt.scatter(data["YEAR"], data["ESTIMATE"])
plt.xlabel("Year")
plt.ylabel("Deaths per 100,000 resident population")
plt.title("Death rates from overdose over year")
plt.xticks(range(int(data["YEAR"].min()), int(data["YEAR"].max()), 2))
plt.show()
