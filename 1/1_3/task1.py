# Необходимо спарсить данные о вакансиях python разработчиков с сайта hh.ru, введя в поиск “python разработчик” и указав, что мы рассматриваем все регионы. Необходимо спарсить:
# Название вакансии
# Требуемый опыт работы
# Заработную плату
# Регион
# И сохранить эти данные в формате json в следующем виде:
# {
#     "data":[
#         {
#             "title":title,
#             "work experience":work_experience,
#             "salary":salary,
#             "region":region
#         }
#     ]
# }

import json
import requests as req
from bs4 import BeautifulSoup as bs
import tqdm

search = "python+разработчик"
url = "https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text="+search+"&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0"
}
data = {
    "data":[]
}

# print(url)
while True:
    # запрос страницы
    page = req.get(url,headers=headers)
    page_soup = bs(page.text,"lxml")
    # список url вакансий
    tags = page_soup.find_all(attrs={"data-qa":"serp-item__title"}, href=True)
    if tags != None:
        for t in tqdm.tqdm(tags):
            print()
            u = t['href']
            if u[0:4] != 'http':
                u = "https://hh.ru"+u
            print(u)
            p = req.get(u,headers=headers)
            p_s = bs(p.text,"lxml")
            title_s = p_s.find(attrs={"data-qa":"vacancy-title"})
            title = ""
            if title_s != None:
                title = title_s.text
            print(title)
            work_experience_s = p_s.find(attrs={"data-qa":"vacancy-experience"})
            work_experience = ""
            if work_experience_s != None:
                work_experience = work_experience_s.text
            print(work_experience)
            salary_s = p_s.find(attrs={"data-qa":"vacancy-salary-compensation-type-net"})
            salary = ""
            if salary_s != None:
                salary = salary_s.text
            print(salary)
            region_s = p_s.find(attrs={"data-qa":"vacancy-view-location"})
            region = ""
            if region_s != None:
                region = region_s.text
            print(region)
            data["data"].append({
                "title":title,
                "work experience":work_experience,
                "salary":salary,
                "region":region
            })
            # запись в файл
            with open('data.json',"w",encoding='utf8') as file:
                json.dump(data,file,ensure_ascii=False)

    # подготовка url перехода на следующую страницу
    tag = page_soup.find(attrs={"data-qa":"pager-next"}, href=True)
    # tag = page_soup.find(attrs={"data-qa":"pager-nextws"}, href=True)
    if tag == None:
        break
    url = tag['href']
    if url[0:4] != 'http':
        url = "https://hh.ru"+url


