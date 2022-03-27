import requests
from webtoon_search import search_webtoon
from bs4 import BeautifulSoup
import csv

week = input("""요일을 선택하세요
mon / tue / wed / thu / fri / sat / sun
: """)
url = f"https://comic.naver.com/webtoon/weekdayList?week={week}"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

webtoons = soup.find("ul", attrs={"class":"img_list"}).find_all("li")

fhandle = open(f"WebtoonList_{week}.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(fhandle)

title = "제목,작가,평점".split(",")
writer.writerow(title)

# 밑의 라인은 다른 파일로 만들어서 간소화
# for webtoon in webtoons:
#     title = webtoon.find("dt").get_text().strip()
#     creator = webtoon.find("dd", attrs={"class":"desc"}).get_text().strip()
#     rating = webtoon.find("div", attrs={"class":"rating_type"}).find("strong").get_text().strip()
#     data = [title, creator, rating]
#     writer.writerow(data)

final_result = search_webtoon(webtoons)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['creator'])
    row.append(result['rating'])
    writer.writerow(row)

fhandle.close()