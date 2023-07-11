#%% Getting the page source
import datetime

import requests
import selectorlib
from scraper_functions import scrape, extractit, store, readit, readit_filepath, extract_beautiful
from send_email import send_email_html
import time
from bs4 import BeautifulSoup


main_url = "http://programmer100.pythonanywhere.com"

# while True:
main_page_source = scrape(main_url)
#%% Testing beautifulsoup
# soup = BeautifulSoup(main_page_source, 'html.parser')
# print(soup.title)
# print(soup.find(id="temperatureId"))
# finder = soup.find(id="temperatureId")
# print(finder)
# tag = BeautifulSoup(str(finder), 'html.parser')
# numberIwant = tag.string
# numberIwant = int(numberIwant)
# print(type(numberIwant))
# print(time.time())
#%% Extract the data and process it
extracted = extract_beautiful(main_page_source, "temperatureId")
extracted = str(extracted)
current_time = time.time()

# Could also try:
# curent_time = datetime.datetime.now()

content_to_store = f"{current_time},{extracted}"
# print(content_to_store, "this is the content to store")
print(f"Extracted string was: {extracted}.")
content = readit_filepath("temps.txt")
#%% Store temp in a file.
store(content_to_store, "temps.txt")

#%% My code
#
#
# beautifulextracted = extract_beautiful(main_page_source, "temperatureId")
# beautifulextracted = str(beautifulextracted)
# beautifulextracted
print(datetime.datetime.now())