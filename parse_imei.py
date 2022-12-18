from bs4 import BeautifulSoup
html_src = open("pages/1.html").read()
soup = BeautifulSoup(html_src, "html.parser")
print(soup.section["section_main"])

