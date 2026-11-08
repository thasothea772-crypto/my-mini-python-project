# Test pandas library part 1
import pandas as pd

def line():
    print("======================================================================")

data = {
    "Year": [2022, 2023, 2024, 2025, 2026],
    "Cloud Cost": [1500, 2000, 2500, 3000, 4000],
    "Server Maintenance": [2000, 2500, 3000, 3500, 5000],
    "Security Software": [2000, 2250, 2500, 3000, 3500],
    "IT Support": [1000, 1190, 2000, 2400, 3000],
}

df = pd.DataFrame(data)
print()
line()
print()
print(df)
print()
line()