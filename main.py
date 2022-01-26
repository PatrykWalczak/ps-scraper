from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

# loop for searching the first five pages

data = []
for page in range(1, 6):
    page_url = "https://polygonscan.com/tokens-nft?p=" + str(page)
    driver.get(page_url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # searching for the necessary elements

    table = soup.find('table', {'class': "table table-text-normal table-hover"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        data.append([ele for ele in cols if ele])               

# Save to csv

df = pd.DataFrame(data, columns= ["Token ID", "Token name", "Transfers (24H)", "Transfers (7D)"])
df.to_csv('polygonscan.csv', index=False, encoding='utf-8')
