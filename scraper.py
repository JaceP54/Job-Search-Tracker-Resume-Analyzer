import requests

def fetch_filtered_jobs(keyword):
    response = requests.get("https://remoteok.com/api")
    data = response.json()[1:]  # Skip metadata at index 0

    filtered_jobs = []

    for job in data:
        title = job.get("position", "").lower()
        tags = ", ".join(job.get("tags", [])).lower()

        if keyword in title or keyword in tags:
            filtered_jobs.append({
                "Position": job.get("position", "N/A"),
                "Company": job.get("company", "N/A"),
                "Location": job.get("location", "N/A"),
                "Tags": ", ".join(job.get("tags", [])),
                "URL": job.get("url", "N/A")
            })

    return filtered_jobs
