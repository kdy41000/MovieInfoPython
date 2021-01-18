import requests
from bs4 import BeautifulSoup


def startcrawling():
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20191207'
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')
    title_list = soup.select('div.info-movie')

    result = []
    for i in title_list:
       # print(i.select_one('a > strong').text.strip()) # a태그 안에 stromg 태그를 찾아서 출력    
       # print(i.select('i')[0].text.strip())
       # print(i.select('i')[1].text.strip())
       # print(i.select('i')[2].text.strip().replace(" ","").rstrip('\n'))
       # print('-----------------------------')
        moviename = i.select_one('a > strong').text.strip()
        jangru = i.select('i')[0].text.strip().replace('\xa0',"")
        opendate = i.select('i')[1].text.strip()
        status = i.select('i')[2].text.strip().replace(" ","").replace('\r\n',"")

        result.append(moviename + '(' + jangru + ') ' + opendate + ' ' + status)
    return result