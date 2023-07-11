#%% Getting the page source
from scraper_functions import scrape, extract_beautiful, store_sql_specific
from send_email import send_email_html
import time
import sqlite3
from bs4 import BeautifulSoup

database_name = "temp_db.db"
connection = sqlite3.connect(database_name)
cursor = connection.cursor()

main_url = "http://programmer100.pythonanywhere.com"

while True:
    main_page_source = scrape(main_url)

    #%% Extract the data and process it
    extracted_temp = extract_beautiful(main_page_source, "temperatureId")
    extracted_temp = str(extracted_temp)
    current_time = time.time()

    content_to_store = [current_time, extracted_temp]

    # print(content_to_store, "this is the content to store")
    print(f"Extracted string was: {extracted_temp}.")

    #%% Store temp in a file.
    store_sql_specific(content_to_store, "temps_db.db", "temps")
    print("Temperature data was stored in temps_db.db successfully.")
    time.sleep(6)

