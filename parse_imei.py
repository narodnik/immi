from bs4 import BeautifulSoup as bs

# get model number
filename = 'pages/1.html'
with open(filename, 'r') as f:
    soup = bs(f, "html.parser")
    s = soup.find_all("ul", class_="list-unstyled mb-0")
    for model in s:
        print(model.text)

# get model names, numbers and IMEI
imei = []
filename = 'pages/1.html'
with open(filename, 'r') as f:
    soup = bs(f, "html.parser")
    s3 = soup.find_all('td')
    for content in s3:
        imei_page1 = content.text
        # print(imei_page1)
        imei.append(imei_page1)
# print(imei)
    new_imei = []
    for each_item in imei:
        new_item = each_item.strip()
        new_imei.append(new_item)
        #print(new_item)

print(new_imei[0])
