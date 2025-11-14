import pandas as pd

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    filtered_data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return filtered_data

# نمونه استفاده
df = pd.DataFrame({'age': [10, 12, 105, 104, 110, 103, 104, 103, 110, 100,1]})
clean_df = remove_outliers_iqr(df, 'age')
print(clean_df)