import requests, time

while True:
    time.sleep(5)
    requests.get("http://picinema.net/film/checkCache/")
    requests.get("http://picinema.net/serietv/checkCache/")