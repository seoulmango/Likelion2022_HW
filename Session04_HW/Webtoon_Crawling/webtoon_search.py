def search_webtoon(webtoons):
    result = []
    for webtoon in webtoons:
        title = webtoon.find("dt").get_text().strip()
        creator = webtoon.find("dd", attrs={"class":"desc"}).get_text().strip()
        rating = webtoon.find("div", attrs={"class":"rating_type"}).find("strong").get_text().strip()
        webtoon_info = {
            'title': title,
            'creator': creator,
            'rating': rating,
        }
        result.append(webtoon_info)
    return result