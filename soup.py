from bs4 import BeautifulSoup
import sqlite3
import requests

response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

output = BeautifulSoup(response.text, 'html.parser')
#output.prettify()

table = output.find("table", class_="wikitable").find("tr")

neighborhoods = []
for row in table.children:
    if (row.name == 'tr'):
        cells = list(row.children)
        if (cells[-2].name == 'td'):
            neighborhoods.extend(cells[-2].getText().split(', '))

conn = sqlite3.connect('soup.db')
c = conn.cursor()
c.execute('''CREATE TABLE neighborhoods
             (name text)''')
for neighborhood in neighborhoods:
    c.execute("INSERT INTO neighborhoods VALUES ('" + neighborhood + "')")
conn.commit()
conn.close() 
