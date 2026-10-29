import requests
from bs4 import BeautifulSoup

# ១. កំណត់ URL របស់វេបសាយដែលចង់ទាញយកទិន្នន័យ
url = "http://quotes.toscrape.com/"

# ២. ប្រើ requests ដើម្បីទាញយកទិន្នន័យពីវេបសាយ
response = requests.get(url)

# ៣. ពិនិត្យមើលស្ថានភាពការតភ្ជាប់ (ប្រសិនបើចេញលេខ 200 មានន័យថាជោគជ័យ)
print("Code:", response.status_code)

# ៤. ប្រើ BeautifulSoup ដើម្បីអានកូដ HTML នោះ
soup = BeautifulSoup(response.text, 'html.parser')

# ៥. រកមើលកន្លែងដែលមានឃ្លា (Quote) ដំបូងគេនៅលើវេបសាយ
first_quote = soup.find('span', class_='text').text

print(first_quote)

from bs4 import BeautifulSoup
import requests

# ១. កំណត់ URL និង Headers ដើម្បីកុំឱ្យ Wikipedia บล็อก (Block)
url = "https://en.wikipedia.org/wiki/Economy_of_Cambodia"
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/115.0.0.0 Safari/537.36'
    )
}

# ២. បញ្ជូន headers ទៅជាមួយ requests.get
response = requests.get(url, headers=headers)

print("Code:", response.status_code)  # គួរតែចេញលេខ 200 (ជោគជ័យ)

# ៣. ប្រើ BeautifulSoup អានកូដ HTML
soup = BeautifulSoup(response.text, 'html.parser')

# ៤. ដកស្រង់ចំណងជើងធំ (Title) របស់ Wikipedia ជំនួសវិញ
# (ព្រោះ Wikipedia គ្មាន span class='text' ដូចវេបសាយមុនទេ)
title = soup.find('span', class_='mw-page-title-main').text

print("Cambodia's Economics:", title)