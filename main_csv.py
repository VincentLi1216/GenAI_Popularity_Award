import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://genaistars.org.tw/vote"
response = requests.get(url)

# BeautifulSoup parse HTML
soup = BeautifulSoup(response.content, "html.parser")

data_list = []

# Find vote items
vote_items = soup.find_all('div', class_='vote_item')

for item in vote_items:
    title = item.find('a', class_='info_title').text.strip()
    count = int(item.find('span').text.strip())
    
    data_list.append({'title': title, 'count': count})

# Sort data
sorted_data = sorted(data_list, key=lambda x: x['count'], reverse=True)

# Output rank to console
title_width = 70
count_width = 10

print(f"{'Rank':<8} {'Count':<{count_width}} {'Title':<{title_width}}")

for i, data in enumerate(sorted_data):
    if data['title'] == 'Lazy Diffusion - 予你閒畫':
        print(f"{i+1:<8} {data['count']:<{count_width}} 🌟{data['title']:<{title_width}}")
    else:
        print(f"{i+1:<8} {data['count']:<{count_width}} {data['title']:<{title_width}}")

print("-" * 100)
print("Our Rank:", [i+1 for i, data in enumerate(sorted_data) if data['title'] == 'Lazy Diffusion - 予你閒畫'][0])

# Save to CSV with ISO timestamp
iso_timestamp = datetime.now().isoformat(timespec='seconds').replace(":", "-")
csv_file = f"vote_results_{iso_timestamp}.csv"
csv_columns = ["Rank", "Title", "Count"]

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()

    for i, data in enumerate(sorted_data):
        writer.writerow({"Rank": i+1, "Title": data['title'], "Count": data['count']})

print(f"Data has been saved to {csv_file}.")
