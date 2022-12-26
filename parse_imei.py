from bs4 import BeautifulSoup as bs
import pandas as pd
import re

tag_info = []
filename = 'pages/1.html'
with open(filename, 'r') as f:
    soup = bs(f, "html.parser")
    tags = soup.find_all('td')
    for content in tags:
        page = content.text
        tag_info.append(page)

imei = []
for each_item in tag_info:
    edited_item = each_item.strip()
    imei.append(edited_item)


lst_final = []
char = '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\t'
for x in imei:
    if char in x:
        item = re.sub(char, ", ", x)
        lst_final.append(item)
    else:
        lst_final.append(x)

colnames = ['IMEI','BRAND','MODELS',]
df = pd.DataFrame(lst_final, columns=['col'])
df.index = [df.index // len(colnames), df.index % len(colnames)]
df = df['col'].unstack()
df.columns = colnames

df.to_csv("test.csv")
