import requests, time

while True:
    time.sleep(5)
    requests.get("http://127.0.0.1:8000/film/checkCache/")
    requests.get("http://127.0.0.1:8000/serietv/checkCache/")