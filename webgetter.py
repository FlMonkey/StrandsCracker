import requests
for i in range(1, 32):
    date = f'2024-03-{0+i}'
    with open(f"GameArchive/{date}.json", 'w') as f:f.write(requests.get(f'https://www.nytimes.com/games-assets/strands/{date}.json').text)
