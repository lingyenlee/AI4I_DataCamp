# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('/Users/apple/Documents/Online_Courses/DataCamp_Excercise/Datasets/dob_job_application_filings_subset.csv')

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))