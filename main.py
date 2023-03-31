# loading data into a pandas dataframe
import pandas as pd
# load the datetime module
import datetime as dt

# Load the CSV file into a pandas dataframe
df = pd.read_csv('raw_data.csv')

# Display the first few rows of the dataframe
print(df.head())

# Checking for missing values in the data
missing_values = df.isnull().sum()

# Print the number of missing values in each column
print("------------------------- Missing Values ----------------------------------")
print(missing_values)

# Check for duplicate records in the dataframe
duplicate_rows = df.duplicated()

# Print the number of duplicate records
print("--------------------------- Number of Duplicated Records ----------------------------")
print(duplicate_rows.sum())

# Dropping the duplicate values:
# Drop duplicate records as a whole
df.drop_duplicates(keep='first', inplace=True)

# Print the cleaned dataframe
print("----------------------- Duplicate Cleaned Dataframe ---------------------------------")
print(df)

# Filling respective values with respective mode

gender_mode = df['gender'].mode()[0]
df['gender'].fillna(gender_mode, inplace=True)

# Fill missing values in marital_status column with mode
marital_status_mode = df['marital_status'].mode()[0]
df['marital_status'].fillna(marital_status_mode, inplace=True)

# Fill missing values in city column with mode
city_mode = df['city'].mode()[0]
df['city'].fillna(city_mode, inplace=True)

# Print the cleaned dataframe
print("----------------------- Filled dataframe with the respective modes -----------------------")
print(df)

# Creating the age column
# Convert dob column to datetime format
df['dob'] = pd.to_datetime(df['dob'])

# Calculate age based on DOB
current_year = dt.date.today().year
df['age'] = current_year - df['dob'].dt.year

# Print the updated dataframe
print(" ----------------------- Dataframe with the Age Included ----------------------------")
print(df)

# Creating new column called income group

# Calculate the 33% percentiles for the income column
percentiles = df['income'].quantile([0.33, 0.66])
print(":::::::::::::::::::::::::::::::::::::::This is the percentiles values::::::::::::::::::::::::::::::::::::::::")
print(percentiles)

print("Percentile Data type")
print(type(percentiles))

# Taking an empty percentile list
percentiles_list = []
print("---------------- Traversing the pandas series ----------------------")
for i in percentiles:
    percentiles_list.append(i)


# Create a function to categorize income values based on percentiles
def income_category(income):
    if income <= percentiles_list[0]:
        return 'Low'
    elif income <= percentiles_list[1]:
        return 'Medium'
    else:
        return 'High'


# Apply the income_category function to the income column to create income_group column
df['income_group'] = df['income'].apply(income_category)

# Print the updated dataframe
print('------------------------- Dataframe with new column income_group included -----------------------')
print(df)


# ---------------------------------------------------------------------------------------------------------
# Creating new column called score_group
# Calculate the 33% percentiles for the income column
score_percentiles = df['income'].quantile([0.33, 0.66])
print(":::::::::::::::::::::::::::::::::::::::This is the percentiles values::::::::::::::::::::::::::::::::::::::::")
print(score_percentiles)

print("Percentile Data type")
print(type(score_percentiles))

# Taking an empty percentile list
scores_percentiles_list = []
print("---------------- Traversing the pandas series ----------------------")
for i in percentiles:
    scores_percentiles_list.append(i)


# Create a function to categorize income values based on percentiles
def score_category(score):
    if score <= scores_percentiles_list[0]:
        return 'Poor'
    elif score <= scores_percentiles_list[1]:
        return 'Fair'
    else:
        return 'Good'


# Apply the income_category function to the income column to create income_group column
df['score_group'] = df['score'].apply(income_category)

# Print the updated dataframe
print('------------------------- Dataframe with new column income_group and score_group included -----------------------')
print(df)

# -----------------------------------------------------------------------------------------------------------------------
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'])
df = df[df['last_purchase_date'].dt.year >= 2019]

print("------------------------------ Dataframe with the last purchase date before 2019 removed -----------------------")
print(df)

# ------------------------------------------------------------------------------------------------------------------------
# save cleaned data to a new CSV file
df.to_csv('clean_data.csv', index=False)
