from bs4 import BeautifulShop
import sqlite3

response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

table = BeautifulSoup(response.text, 'html.parser')

print (table['wikitble']) 
