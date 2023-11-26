from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())            # Prints the entire html code with indentation

match = soup.title                  # Prints title with <tags>
print(match)

match1 = soup.title.text             # Prints just the text of the title
print(match1)

match2 = soup.find('div')
print(match2)

match3 = soup.find('div', class_ = 'footer')
print(match3)

article = soup.find('div', class_ = 'article')
print(article)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

for article in soup.find_all('div', class_ = 'article'):
    print()
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)


# Trying on a real world website

source = requests.get('https://brianyu.me/videos').text

soup1 = BeautifulSoup(source, 'lxml')
# print(soup1.prettify())

titl = soup1.title.text
print(titl)

# article = soup1.find('div')
# print(article.prettify())

vid_src = soup1.find('iframe', class_ = 'absolute border-0 w-full h-full')['src']
print(vid_src)

vid_id = vid_src.split('/')[4]
print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)