#%% Imports
import requests
import selectorlib
from scraper_functions import store, store_sql, scrape, extract_beautiful, readit_sql,  readit_filepath
from send_email import send_email_html
import time
import sqlite3
#%% Get the page source data

main_url = "http://programmer100.pythonanywhere.com/tours/"

while True: # This is what you need to add to make the code run continously.
    main_page_source = scrape(main_url)

    #%% Extract the data and process it
    extracted = extract_beautiful(main_page_source, "displaytimer")
    extracted = str(extracted)
    print(f"Extracted string was: {extracted}.")
    #%% Trigger e-mail delivery on certain conditions

    if extracted != "No upcoming tours":
        extracted_row, existing_content = readit_sql(extracted)
        if existing_content:
            print("Content exists. Duplicate tour dates will not be added to database.")
        if not existing_content: # If there are no such rows like this in the database
            store_sql(extracted_row, "events")
            send_email_html("A new tour date was added!", message=f"<h1>{extracted}</h1> was added to the band's touring schedule!")
            print("E-mail was sent!")

    time.sleep(2) # This is to make sure you don't accidentally DDOS the page you're scraping, or, more likely, get yourself IP banned.

#%%
