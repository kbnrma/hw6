import time
import requests
import schedule

URL = "https://geeksbackend.notion.site/geeksbackend/Geeks-Backend-2b37c7cbcfe240198c1d522b045a69c3"
INITIAL_DELAY = 5
REQUEST_INTERVAL = 10

def perform_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print(f"Request to {url} successful. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error during request to {url}: {e}")

def main():
    perform_request(URL)
    schedule.every(REQUEST_INTERVAL).seconds.do(perform_request, URL)
    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    print("HTTP Request Scheduler started.")
    time.sleep(INITIAL_DELAY)
    main()