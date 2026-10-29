# First project
import pandas as pd # pandas is a library that we use it to convert data row to data column

# Create the data of expenses for 4 years
data = { # it is dictionary
    'Year': [2023, 2024, 2025, 2026],
    'Cloud Cost': [2000, 5000, 10000, 20000],
    'Server Maintenance': [4000, 7000, 15000, 30000]
}

# Insert data that it call dictionary to pandas DataFrame
df = pd.DataFrame(data) # DataFrame is a class that convert the data row to data column

# Calculate the total cost
df['Total Cost'] = df['Cloud Cost'] + df['Server Maintenance']

# Show the Data
print("--- Data ---")
print(df)

# Second project
print("\n")
import pandas as pd

# Create the data the it calls dictionary
data = {
    'Tool Name': ['Cloud Server', 'Database Hosting', 'Security Software', 'Demain & SSL'],
    'Category': ['Infrastructure', 'Infrastructure', 'Security', 'Network'],
    'Monthly Cost': [400, 450, 500, 900],
    'User': [50, 60, 70, 80]
}

# Create the DataFrame that it users for converting the data row to data column
df = pd.DataFrame(data)

# Calculate the expenses annual of each device (for 12 months: Monthly Cost * 12)
df['Annual Cost'] = df['Monthly Cost'] * 12

# Show the whole result
print("\t\t\t\t--- Data ---")
print(df)

# Just only show the infrastructure category
infras_df = df[df['Category'] == 'Infrastructure']
print("\n\t\t\t --- Infrastructure ---")
print(infras_df)

# Show the most highest device
max_cost = df['Annual Cost'].max()
print(f"\nThe highest expenditure is: ${max_cost}")