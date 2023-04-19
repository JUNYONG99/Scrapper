from bs4 import BeautifulSoup
import requests


def extract_jobs_weworkremotely(term):
    url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all("li", class_="feature")
            for post in job_posts:
                company = post.find("span", class_="company")
                position = post.find("span", class_="title")
                location = post.find("span", class_="region")
                if company:
                    company = company.string.strip()
                if position:
                    position = position.string.strip()
                if location:
                    location = location.string.strip()
                if company and position and location:
                    job_data = {
                        'company': company,
                        'position': position,
                        'location': location
                    }
                    results.append(job_data)
    else:
        print("Can't get jobs.")

    return results
