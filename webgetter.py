import requests
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.nytimes.com/games/strands',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
}

current_date = '2024-03-10'
response = requests.get(f'https://www.nytimes.com/games-assets/strands/{current_date}.json', headers=headers)

with open("answers.json", 'w') as f:
    f.write(response.text)