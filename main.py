#%% Imports
import requests
import selectorlib
from scraper_functions import scrape, extractit, store, readit
from send_email import send_email_html
import time

#%% Get the page source data

main_url = "http://programmer100.pythonanywhere.com/tours/"

while True: # This is what you need to add to make the code run continously.
    main_page_source = scrape(main_url)

    #%% Extract the data and process it
    extracted = extract_beautiful(main_page_source)
    print(f"Extracted string was: {extracted}.")
    content = readit("data.txt")
    #%% Trigger e-mail delivery on certain conditions

    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted, "data.txt")
            send_email_html("A new tour date was added!", message=f"<h1>{extracted}</h1> was added to the band's touring schedule!")
            print("E-mail was sent!")

    time.sleep(2) # This is to make sure you don't accidentally DDOS the page you're scraping, or, more likely, get yourself IP banned.

#%%
