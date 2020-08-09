import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def scrape_hospitals():
    response = requests.get('https://qz.com/1518545/price-lists-for-the-115-biggest-us-hospitals-new-transparency-law/')
    if response.status_code == 200:
        content = response.content

        soup = bs(content, features="html.parser")
        table = soup.find_all('td')
    
        df_row_list = []

        for row in table:
        
            row =str(row)
            split_line = row.split("\"")
            
            url = split_line[1].strip()

            name = split_line[-1].strip()
            name = re.search('>(.*)<', name).group(1).strip('</a>').strip()
            
            row_dict = {}
            row_dict['Name'] = name
            row_dict['URL'] = url
            df_row_list.append(row_dict)
 
            
    df = pd.DataFrame(df_row_list)
    df.to_csv('hospitals.csv',header=['Name','URL'],index=False)

scrape_hospitals()
