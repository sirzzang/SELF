import os
import tarfile # tar 파일을 읽고 쓸 수 있는 모듈
import urllib # python 3 : urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/" 
HOUSING_PATH = os.path.join("data", "handson-ml", "housing", "")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path): # 파일 저장 경로 없으면 만들기
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz") # tgz파일 받을 경로
    urllib.request.urlretrieve(housing_url, tgz_path) # urlretrieve를 통해 바로 저장.
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close() # 파일 닫기

fetch_housing_data()