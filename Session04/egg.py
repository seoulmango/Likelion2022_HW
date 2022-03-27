import requests
from bs4 import BeautifulSoup

# 우리가 정보를 얻고 싶어하는 URL
pagenum = 1
def EGG_URL(page_num):
    return f"https://search.shopping.naver.com/search/all?pagingIndex={pagenum}&pagingSize=80&query=반숙란"
# get 요청을 통해 해당 페이지 정보를 저장

EGG_URL = EGG_URL(1)

egg_html = requests.get(EGG_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
egg_soup = BeautifulSoup(egg_html.text,"html.parser")


egg_list_box = egg_soup.find("ul",{"class":"list_basis"})
egg_list = egg_list_box.find_all("li",{"class":"basicList_item__2XT81"})
result = []
title = egg_list[0].find("div",{"class":"basicList_title__3P9Q7"}).find("a").string
price = egg_list[0].find("span",{"class":"price_num__2WUXn"}).text
detail_lists = egg_list[0].find("div",{"class":"basicList_detail_box__3ta3h"}).find_all("a")

detail = []
for detail_list in detail_lists:
    detail.append(detail_list.text)


result = {
    "title": title,
    "price": price,
    "detail": detail,
}
for i in range(1,11):
    EGG_URL(i)
    print(result)
    pagenum += 1