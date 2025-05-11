# Create a Series from a list
import pandas as pd
data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data)
print(series_from_list)

# Create an empty Series
import pandas as pd
empty_series = pd.Series()
print(empty_series)

import pandas as pd

# Create a DataFrame from a list of lists
data = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 35]
]

# Create the DataFrame
columns = ['ID', 'Name', 'Age']
df_from_list = pd.DataFrame(data, columns=columns)
print(df_from_list)


# Create a dictionary where keys are column names and values are lists of data
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)