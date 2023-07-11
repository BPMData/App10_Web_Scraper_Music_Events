import requests
import selectorlib

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

def store(extracted_data, savefilename1):
    with open(f"{savefilename1}", "a") as file:
        print(f"{extracted_data} was stored.")
        file.write(extracted_data + "\n")

# def readit(savefilename2):
#     with open(f"{savefilename2}", "r") as file:
#         print(f"{savefilename2} was read.")
#         return file.read()

def readit(extracted):
    with open("data.txt", "r") as file:
        return file.read()