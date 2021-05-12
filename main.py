import requests
from bs4 import BeautifulSoup

response = requests.get('https://qz.com/africa/latest/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#html
posts = site.findAll('li', attrs={'class':'_8OV9v _1dOXL'})

for post in posts:

    #titulo
    title = post.find('div', attrs={'class':'f01AT aGNvr _5yjC0'})

    print(title.text)

    #link
    link = post.find('a', attrs={'class':'eBKpx'})

    print(link['href'])




