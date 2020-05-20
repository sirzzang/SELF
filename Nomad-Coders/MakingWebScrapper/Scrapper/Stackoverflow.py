# module import
import requests
from bs4 import BeautifulSoup

# 변수
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True) # page[-1] : 마지막 Next, page[-2] : 그 이전 마지막 페이지
    return int(last_page)

def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-")
    job_id = html["data-jobid"]
    link = f"https://stackoverflow.com/jobs/{job_id}"
    return {'title' : title, 'company' : company, 'location' : location, 'link' : link}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page+1}")
        req = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(req.text, 'lxml')
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result) # 위의 함수로 result 넘김.
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs