# A Web crawler consists of a computer program that browses the Web to
# search for information on pages. The scenario to be analyzed is a
# problem in which a sequential Web crawler is fed by a variable number
# of Uniform Resource Locators (URLs), and it has to search all the links
# within each URL provided. Imagining that the number of input URLs may
# be relatively large, we could plan a solution looking for parallelism
# in the following way:

# 1. Group all the input URLs in a data structure.
# 2. Associate data URLs with tasks that will execute the crawling by
# obtaining information from each URL.
# 3. Dispatch the tasks for execution in parallel workers.
# 4. The result from the previous stage must be passed to the next stage,
# which will improve raw collected data, thereby saving them and relating
# them to the original URLs.

# coding: utf-8

import concurrent.futures
import logging
import queue
import re
import sys
import threading

import requests
from cytoolz.itertoolz import remove

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# get html link as <a ... href="..." ... >
html_link_regex = \
    re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')

urls = queue.Queue()
urls.put('http://www.google.com')
urls.put('http://br.bing.com/')
urls.put('https://duckduckgo.com/')
urls.put('https://github.com/')
urls.put('http://br.search.yahoo.com/')

urls.put('http://www.foxnews.com/')
urls.put('http://www.cnn.com/')
urls.put('http://europe.wsj.com/')
urls.put('http://www.bbc.co.uk/')
urls.put('http://some-made-up-domain.com/')

result_dict = {}


def group_urls_task(urls):
    try:
        # get an url ; block if necessary until an item (url) is available.
        url = urls.get(True, 0.05)
        result_dict[url] = None
        logger.info("[%s] putting url [%s] in dictionary..." % (
            threading.current_thread().name, url))
    except queue.Empty:
        logging.error('Nothing to be done, queue is empty')


def crawl_task(url):
    links = []
    try:
        # get web content from url
        request_data = requests.get(url)
        logger.info("[%s] crawling url [%s] ..." % (
            threading.current_thread().name, url))
        # get all links in web content accept url itself and null string
        links = remove(lambda x: x == url or x == '',
                       html_link_regex.findall(request_data.text))
    except:
        logger.error(sys.exc_info()[0])
        raise
    finally:
        return (url, links)  # `links` is toolz's remove object

# create a ThreadPool named `group_link_threads` to execute `group_urls_task`
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as group_link_threads:
    for i in range(urls.qsize()):
        group_link_threads.submit(group_urls_task, urls)

# create a ThreadPool named `crawler_link_threads` to execute `crawl_task`
# for `urls`
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as crawler_link_threads:
    future_tasks = {crawler_link_threads.submit(
        crawl_task, url): url for url in result_dict.keys()}
    for future in concurrent.futures.as_completed(future_tasks):
        result_dict[future.result()[0]] = future.result()[1]

for url, links in result_dict.items():
    try:
        logger.info("[%s] with links : [%s..." % (url, max(links, key=len)))
    except ValueError:
        logger.info("[%s] with links : [%s..." % (url, links))
