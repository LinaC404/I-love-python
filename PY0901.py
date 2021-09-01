import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

'''
print(soup.title)
print(soup.p.parent.name)

tag = soup.a
print(tag.attrs['id'])
print(type(tag))

newsoup = BeautifulSoup("<b><!--This is a comment!--></b><p>This is not a comment</p>","html.parser")
print(newsoup.b.string)
print(newsoup.p.string)


print(soup.head)
print(soup.head.contents)
print(soup.body.contents,len(soup.body.contents))
'''

print(soup.prettify())