import requests, time

while True:
    time.sleep(5)
    requests.get("http://0.0.0.0/film/checkCache/")
    requests.get("http://0.0.0.0/serietv/checkCache/")