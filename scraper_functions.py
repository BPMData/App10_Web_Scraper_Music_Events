import requests
import selectorlib
from bs4 import BeautifulSoup
import sqlite3
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Create a connection to our database
database_name = "test_01.db"
connection = sqlite3.connect(database_name)
cursor = connection.cursor()


def scrape(url):
    """Scrape the page source from a given URL."""
    response = requests.get(url, headers=HEADERS)
    page_source = response.text
    return page_source

def extractit(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

# def extract_specific(source, keyname, css_selector):
#     desired_data = f"""
#     {keyname}:
#         css:{css_selector}
#     """
#     extractor = selectorlib.Extractor.from_yaml_string(desired_data)
#     value = extractor.extract(source)[f"{keyname}"]
#     return value

def extract_beautiful(source, css_selector):
    """Do NOT put a hashtag in the CSS selector!
    displaytimer is right.
    #displaytimer is NOT right."""

    soup = BeautifulSoup(source, 'html.parser')
    finder = soup.find(id=css_selector)
    tag = BeautifulSoup(str(finder), 'html.parser')
    value_to_return = tag.string
    return value_to_return

def store(extracted_data, savefilename1):
    with open(f"{savefilename1}", "a") as file:
        print(f"{extracted_data} was stored.")
        file.write(extracted_data + "\n")

def store_sql(extracted_data, tablename):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {tablename} VALUES(?,?,?)", extracted_data)
    connection.commit()

def store_sql_specific(extracted_data, databasename, tablename):
    database_name = "temp_db.db"
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {tablename} VALUES(?,?)", extracted_data)
    connection.commit()

def readit_filepath(savefilename2):
    with open(f"{savefilename2}", "r") as file:
        print(f"{savefilename2} was read.")
        return file.read()

def readit(extracted):
    with open("data.txt", "r") as file:
        return file.read()

def readit_sql(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band_name=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return row, rows



