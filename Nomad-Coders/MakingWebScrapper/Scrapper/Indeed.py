# module import
import requests
from bs4 import BeautifulSoup

# 변수
LIMIT = 50  # 게시물 몇 개씩 표시할 것인지 변경 가능
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


# 마지막 페이지 호출
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


# html 페이지에서 정보 추출하는 함수. dict 반환.
def extract_job(html):
    # 직무
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    # 회사명
    try:
        company = html.find("span", {"class": "company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    except AttributeError as e:
        print(f"회사명이 없는 공고가 있습니다.")
        company = "No Information"
    # 위치
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    # 지원하기 링크
    job_id = html["data-jk"]
    link = f"https://www.indeed.com/viewjob?jk={job_id}"  # indeed.com에서 jk 다음에 id.
    return {'title': title, 'company': company, 'location': location, "link": link}


# 모든 페이지 스크레이핑
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page + 1}")  # 확인용
        req = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


# 모든 함수
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs