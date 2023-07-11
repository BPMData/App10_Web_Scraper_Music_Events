import requests
import selectorlib
from bs4 import BeautifulSoup
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from a given URL."""
    response = requests.get(url, headers=HEADERS)
    page_source = response.text
    return page_source

def extractit(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def extract_specific(source, keyname, css_selector):
    desired_data = f"""
    {keyname}:
        css:{css_selector}
    """
    extractor = selectorlib.Extractor.from_yaml_string(desired_data)
    value = extractor.extract(source)[f"{keyname}"]
    return value

def extract_beautiful(source, css_selector):
    soup = BeautifulSoup(source, 'html.parser')
    finder = soup.find(id=css_selector)
    tag = BeautifulSoup(str(finder), 'html.parser')
    value_to_return = tag.string
    return value_to_return

def store(extracted_data, savefilename1):
    with open(f"{savefilename1}", "a") as file:
        print(f"{extracted_data} was stored.")
        file.write(extracted_data + "\n")

def readit_filepath(savefilename2):
    with open(f"{savefilename2}", "r") as file:
        print(f"{savefilename2} was read.")
        return file.read()

def readit(extracted):
    with open("data.txt", "r") as file:
        return file.read()