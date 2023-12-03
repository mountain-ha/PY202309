import requests
from bs4 import BeautifulSoup as bs
from collections import Counter

#url열기
url = 'https://quotes.toscrape.com/tag/life/'
response = requests.get(url)

# 명언에서 텍스트 추출
soup = bs(response.text, 'html.parser')
quotes = soup.find_all('div', {"class": "quote"})
quote_texts = [quote.find('span', {"class": "text"}).text for quote in quotes]

#토큰 빈도수가 저장된 딕셔너리 생성
quotes_text = ' '.join(quote_texts)
terms_list = quotes_text.lower().split()
term_frequency_dict = dict(Counter(terms_list))

sorted_term_frequency = dict(sorted(term_frequency_dict.items(), key=lambda x: x[1], reverse=True))

# 상위 5개 용어 출력
print("-----상위 5개 용어-----")
for idx, (term, frequency) in enumerate(sorted_term_frequency.items(), start=1):
    print(f"{idx}. {term}: {frequency} 회")
    if idx == 5:
        break