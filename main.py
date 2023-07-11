#%% Getting the page source
import requests
import selectorlib
from scraper_functions import scrape, extractit, store, readit
from send_email import send_email_html


main_url = "http://programmer100.pythonanywhere.com/tours/"

main_page_source = scrape(main_url)
# Hey it worked! It is like RStudio. Nice!
#%% Extract the data and process it
extracted = extractit(main_page_source)
print(f"Extracted string was: {extracted}.")
content = readit("data.txt")
#%% Trigger e-mail delivery on certain conditions

if extracted != "No upcoming tours":
    if extracted not in content:
        store(extracted, "data.txt")
        send_email_html("A new tour date was added!", message=f"<h1>{extracted}</h1> was added to the band's touring schedule!")
        print("E-mail was sent!")
