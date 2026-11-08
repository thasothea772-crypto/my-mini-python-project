import pandas as pd

# ជំហានទី១៖ បង្កើតទិន្នន័យថវិកា និងការចំណាយលើ IT
data = {
    'Tool_Name': [
        'Cloud Server',
        'Database',
        'Security Software',
        'Domain & Hosting',
        'ERP System',
    ],
    'Category': [
        'Infrastructure',
        'Infrastructure',
        'Security',
        'Network',
        'Software',
    ],
    'Monthly_Cost': [400, 250, 120, 30, 600],
    'Users_Count': [150, 150, 300, 300, 50],
}

# បម្លែងជា Pandas DataFrame
df = pd.DataFrame(data)

print('========================================')
print("     data's table expenses on IT        ")
print('========================================')
print(df)
print('\n')

# ជំហានទី២៖ គណនាតម្លៃសេដ្ឋកិច្ច (Economic Calculations)
# បង្កើតជួរឈរថ្មី 'Annual_Cost' (តម្លៃប្រចាំឆ្នាំ)
df['Annual_Cost'] = df['Monthly_Cost'] * 12

# គណនាថវិកាសរុបដែលត្រូវចំណាយក្នុងមួយឆ្នាំ
total_budget = df['Annual_Cost'].sum()
print(f'Total budget of IT : ${total_budget}')

# គណនាថ្លៃចំណាយមធ្យមប្រចាំខែ
avg_monthly = df['Monthly_Cost'].mean()
print(f' The average monthly expenses on each tools: ${avg_monthly}')
print('\n')

# ជំហានទី៣៖ การតម្រៀបទិន្នន័យ (Sorting) - រកមើលឧបករណ៍ស៊ីថវិកាច្រើនជាងគេ
print('========================================')
print('  ====================================  ')
print('========================================')
sorted_df = df.sort_values(by='Annual_Cost', ascending=False)
print(sorted_df)
print('\n')

# ជំហានទី៤៖ ការត្រងទិន្នន័យ (Filtering) - យកតែប្រភេទ Infrastructure
print('========================================')
print('     Category Infrastructure     ')
print('========================================')
infra_df = df[df['Category'] == 'Infrastructure']
print(infra_df)