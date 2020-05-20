import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="UTF-8") # 없으면 현재 경로에 파일 생성
    writer = csv.writer(file) # 방금 연 파일에 csv 작성
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    file.close()
    return