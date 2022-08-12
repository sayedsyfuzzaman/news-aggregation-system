from bs4 import BeautifulSoup
import requests

key = input('Type here to search: ')

link='https://en.prothomalo.com/search?q='+key

html_text = requests.get(link).text
soup = BeautifulSoup(html_text, 'lxml')

all_news = soup.find_all('div', class_='left_image_right_news news_item leftImageRightNews-m__base__c1lVS')

for news in all_news:
    news_title_block = news.find('div', class_='content-area')
    news_title = news_title_block.h3.a.text
    upload_time = news.find('time', class_='published-time publishedAt-m__published-at__2eHYg')
    discription = news.find('p', class_='excerpt excerpt-m__excerpt__2Y5mz')
    more_info = news.h3.a['href']
    image_block = news.find('picture')
    image = image_block
    print(f'''
    News title: {news_title}
    News discription: {discription.text}
    More info: {more_info}
    News upload time: {upload_time.text}
    image: {image}
    ''')
