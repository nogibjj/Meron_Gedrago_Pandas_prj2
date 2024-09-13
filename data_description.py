# import packages
import pandas as pd
import matplotlib.pyplot as plt

# read csv file


def load_dataset(dataset):
    dataset = "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
    data_set = pd.read_csv(dataset)
    data = data_set[
        (data_set["STUB_NAME"] == "Total")
        & (data_set["AGE"] == "All ages")
        & (data_set["PANEL"] == "All drug overdose deaths")
        & (data_set["UNIT"] == "Deaths per 100,000 resident population, crude")
    ]

    return data


# calculating mean, median and mode
# def summary_stats(data):
#    mean = data["ESTIMATE"].mean()
#    median = data["ESTIMATE"].median()
#    std = data["ESTIMATE"].std()
#    print (f"This is the mean is {mean};
#    This is the median is {median};
#    This is the standard deviation is {std}")


def create_mean(data):
    mean = data["ESTIMATE"].mean()
    return f"This is the mean is {mean}"


def create_median(data):
    median = data["ESTIMATE"].median()
    return f"This is the median is {median}"


def create_std(data):
    std = data["ESTIMATE"].std()
    return f"This is the standard deviation is {std}"


def create_graph(data):
    # Create visualization
    plt.scatter(data["YEAR"], data["ESTIMATE"])
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100,000 resident population")
    plt.title("Death rates from overdose over year")
    plt.xticks(range(int(data["YEAR"].min()), int(data["YEAR"].max()), 2))
    plt.show()


# print(create_graph(data))
