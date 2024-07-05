import pandas as pd

# Read data from CSV files into DataFrames
df1 = pd.read_csv('SpEffectParam2.csv')
df2 = pd.read_csv('SpEffectParam.csv')

# Step 1: Identify columns from df1 to transfer or add to df2
columns_to_transfer = df1.columns

# Step 2: Modify df2
# Add missing columns from df1 to df2 with empty values
for col in columns_to_transfer:
    if col not in df2.columns:
        df2[col] = ''

# Drop columns in df2 that are not in df1
columns_to_drop = [col for col in df2.columns if col not in columns_to_transfer]
df2.drop(columns=columns_to_drop, inplace=True)

# Step 3: Ensure columns order is the same as in df1
df2 = df2[columns_to_transfer]

df2.to_csv('path_to_output_file.csv', index=False)