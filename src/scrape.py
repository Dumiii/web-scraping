import sys
import pprint as pp
import requests
import pyttsx3 as tts

from bs4 import BeautifulSoup

def get_news(page_num):
    endpoint = "https://news.ycombinator.com"
    if page_num > 1:
        endpoint += f"/?p={page_num}"

    return requests.get(endpoint, timeout=5)

def extract_from_soup(page_num):
    data = get_news(page_num)
    soup = BeautifulSoup(data.text, 'html.parser')
    titles = soup.select(".titleline > a")
    subtext = soup.select(".subtext")
    return (titles, subtext)

def filter_top_news(num_pages):
    news = []
    # start at 1 to prevent getting first page twice
    for i in range(1, num_pages+1):
        titles, subtext = extract_from_soup(i)
        for i, item in enumerate(titles):
            title = item.getText()
            link = item.get("href")
            score = subtext[i].select(".score")
            if len(score):
                score_num = int(score[0].getText().split(" ")[0])
                if score_num > 100:
                    news.append({
                        "title": title,
                        "link": link,
                        "score": score_num
                    })
    return news

def main(num_pages):
    engine = tts.init()
    # default rate is set to 200 which is too fast
    engine.setProperty('rate', 100)
    top_news = filter_top_news(num_pages)
    top_news.sort(key=lambda x:x["score"], reverse=True)
    for news in top_news:
        engine.say(news["title"])
        engine.runAndWait()
        pp.pprint(news)

if __name__ == '__main__':
    main(int(sys.argv[1]))
