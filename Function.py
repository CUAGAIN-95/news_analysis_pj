#뉴스타이틀 크롤링을 위한 모듈 import
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib import parse

# 뉴스타이틀 크롤링한 뒤 제목 리스틑 리턴
def news_title_crawling(dates, base_url, news_block, news_title_block) -> list:
    result_list = []
    error_cnt = 0
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    for date in dates:
        for page in range(1, 3):
            url = base_url.format(date, page)
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text)
                title_list = soup.select(news_block)
                for title in title_list:
                    try:
                        news_title = title.select_one(news_title_block).text.strip()
                        find_1 = news_title.find("[")
                        find_2 = news_title.find("]")
                        if find_1 != -1:
                            slice_news_title = news_title[find_1:find_2+1]
                            news_title.strip(slice_news_title)
                            result_list.append([news_title.strip(slice_news_title).strip()])
                        elif find_1 == -1:
                            result_list.append([news_title])
                    except:
                        error_cnt += 1
    return result_list
