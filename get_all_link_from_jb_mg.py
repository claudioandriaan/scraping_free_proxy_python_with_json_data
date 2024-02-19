import requests
from bs4 import BeautifulSoup
import pandas as pd

max_page = 5
all_links = []

for page in range(1, max_page + 1):    
    url = f"https://www.portaljob-madagascar.com/emploi/liste/page/{page}"
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('article', class_="item_annonce"):
            lien = link.find('a').get('href')
            all_links.append(lien)
    else:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")

df = pd.DataFrame({'Liens': all_links})

df.to_excel('liens_emplois.xlsx', index=False)

print("Fichier Excel créé avec succès.")
