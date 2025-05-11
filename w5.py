import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)

# Accessing the index
print(df.index)


# Set 'Name' column as the index
df_with_index = df.set_index('Name')
print(df_with_index)

# Reset the index back to the default integer index
df_reset = df.reset_index()
print(df_reset)

row = df_with_index.loc['Alice']  # Assuming 'Name' is the index
print(row)

#Change the index
df_with_new_index = df.set_index('Age')
print(df_with_new_index)

print(df)

# Accessing specific rows and columns
age_column = df['Age']
print(age_column)

second_row = df.iloc[1]
print(second_row)

subset = df.loc[0:2, ['Name', 'Age']]
print(subset)

filtered_data = df[df['Age'] > 25]
print(filtered_data)

salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)