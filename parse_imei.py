from bs4 import BeautifulSoup
html_src = open("pages/1.html").read()
soup = BeautifulSoup(html_src, "html.parser")

# Lookup a tag in HTML code:
#
#  <section id="section_main" class="mb-4">
#
print(soup.section["section_main"])

