from django.test import TestCase

# Create your tests here.
import json



# ret=json.loads('"trues"')
# print(ret)
# print(type(ret))


s="<div><div>Hello</div><p>Yuan</p></div><a>click</a><script>alert(123)</script>"

from bs4 import BeautifulSoup

soup=BeautifulSoup(s,"html.parser")
# print(soup.text)

for tag in soup.find_all():
    # print(tag.name)

    if tag.name=="script":
        tag.decompose()

print(str(soup))