from bs4 import BeautifulSoup as bs

# get model number

filename = 'pages/1.html'
with open(filename, 'r') as f:
    soup = bs(f, "html.parser")
    s = soup.find_all("ul", class_="list-unstyled mb-0")
    for model in s:
        print(model.text)
