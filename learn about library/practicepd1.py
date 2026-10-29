# Using Library pandas
import pandas as pd

def line():
    print("==================================================================================================================================================================")

data_score = {
    'Name': ['Tha Sothea', 'Vy Sokimsa', 'Sok Somaliza', 'Vol limol', 'Ream Phyban', 'Han Sengheang'],
    'Web Development': [90, 95, 85, 80, 90, 80],
    'Business English': [85, 90, 80, 75, 80, 85],
    'Financial Accounting': [95, 95, 90, 85, 90, 90],
    'Princioles of management': [90, 90, 80, 85, 80, 85],
    'Python': [95, 90, 85, 80, 80, 85],
    'UX/UI Design': [90, 90, 80, 85, 85, 80]
}

df = pd.DataFrame(data_score)

df['Total Score'] = (df['Web Development'] + df['Business English'] + df['Financial Accounting'] + 
                   df['Princioles of management'] + df['Python'] + df['UX/UI Design'])

df['Avg Score1'] = (df['Web Development'] + df['Business English'] + df['Financial Accounting'] + 
                   df['Princioles of management'] + df['Python'] + df['UX/UI Design'])/6

df['Avg Score2'] = (df['Total Score']) / 6
print()
print("\t\t\t\t\t\t\t------------- Data -------------")
line()
print()
print(df)
print()
line()
