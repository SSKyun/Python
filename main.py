from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extracts_wwr_job

base_url = "https://kr.indeed.com/jobs?q=python"
search_term = "python"
print(base_url)
response = get(f"{base_url}")

if response.status_code != 200:
    print("Can't response")
else:
    print(response.text)