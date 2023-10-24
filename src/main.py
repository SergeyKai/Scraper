from bs4 import BeautifulSoup
import requests


url = 'https://ru.freepik.com/photos/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

response = requests.get(
    url,
    headers=headers,
)

soup = BeautifulSoup(response.text, 'html.parser')

img_containers = soup.find_all('figure', 'showcase__item')

img_urls = []

for img_container in img_containers:
    # img_url = img_container.find('img')['data-src']
    img_urls.append(
        img_container['data-image']
    )

print(img_urls)
