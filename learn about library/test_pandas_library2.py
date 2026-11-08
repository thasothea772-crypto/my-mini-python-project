# Test pandas library part 2
import pandas as pd

def line(a):
    print(f"=================== {a} ===================")

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

print()
df = pd.DataFrame(data)
line("Welcome to your database")
print(df)
print()