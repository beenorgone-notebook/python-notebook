import time

import deco
import requests


urls = """
https://www.peterbe.com/plog/blogitem-040212-1
https://www.peterbe.com/plog/geopy-distance-calculation-pitfall
https://www.peterbe.com/plog/app-for-figuring-out-the-best-car-for-you
https://www.peterbe.com/plog/Mvbackupfiles
https://www.peterbe.com/plog/swedish-holidays-explaine
https://www.peterbe.com/plog/wing-ide-versus-jed
https://www.peterbe.com/plog/worst-flash-site-of-the-year-2010
""".strip().splitlines()


@deco.concurrent
def download(url, data):
    t0 = time.time()
    assert requests.get(url).status_code == 200
    t1 = time.time()
    data[url] = t1 - t0


@deco.synchronized
def run(data):
    for url in urls:
        download(url, data)


somemute = {}
t0 = time.time()
run(somemute)
t1 = time.time()
print("TOOK", t1 - t0)
print("WOULD HAVE TAKEN", sum(somemute.values()), "seconds")
