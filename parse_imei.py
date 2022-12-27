#TODO
# DF - sort when none are not first to display
# DF - get rid of the index column

from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import os
import numpy as np

files_list = []
file_path = "./pages/"
for root, directories, files in os.walk(file_path):
    for name in files:
        files_list.append(os.path.join(root, name))

print(f"Parsing the data from {file_path} . . .")

tag_info = []
for each_file in files_list:
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

print(f"Sorting imeis into a DataFrame (csv). . .")

lst = []
char = '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\t'
for x in imei:
    if char in x:
        item = re.sub(char, ", ", x)
        lst.append(item)
    else:
        lst.append(x)


colnames = ['IMEI','BRAND','MODELS']
df = pd.DataFrame(lst, columns=['col'])
df.index = [df.index // len(colnames), df.index % len(colnames)]
df = df['col'].unstack()
df.columns = colnames
df = df.replace('', np.nan)
srt_df = df.sort_values(by=['BRAND'])
name = 'imei_sheet.csv'
srt_df.to_csv(name, index=False)

print(f"The content was parsed and exported to {name}.")