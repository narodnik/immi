from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import os

files_list = []
file_path = "./pages/"
for root, directories, files in os.walk(file_path):
    for name in files:
        files_list.append(os.path.join(root, name))

print(f"Parsing the data from the webpage . . .")

tag_info = []
for each_file in files_list[:1]:
    with open(each_file, 'r') as f:
        soup = bs(f, "html.parser")
        tags = soup.find_all('td')
        for content in tags:
            page = content.text
            tag_info.append(page)

imei = []
for each_item in tag_info:
    edited_item = each_item.strip()
    imei.append(edited_item)

lst = []
char = '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\t'
for x in imei:
    if char in x:
        item = re.sub(char, ", ", x)
        lst.append(item)
    else:
        lst.append(x)

lst_final = []
for item in lst:
    if item != '':
        lst_final.append(item)

colnames = ['IMEI','BRAND','MODELS']
df = pd.DataFrame(lst_final, columns=['col'])
df.index = [df.index // len(colnames), df.index % len(colnames)]
df = df['col'].unstack()
df.columns = colnames
srt_df = df.sort_values(by = 'BRAND')
name = 'imei_sheet.csv'
srt_df.to_csv(name)

print(f"The content was parsed and exported to {name}.")