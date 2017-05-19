from bs4 import BeautifulSoup

soup = BeautifulSoup(open('html.html'))
print soup.prettify()
print ('This is leader:\n\n')
print soup.title
print ('\n\n')
print soup.head
print ('\n\n')
print soup.a
print ('\n\n')
print soup.p

print type(soup.a)
print soup.name
print soup.p.attrs
print soup.p.get('class')
soup.p['class'] = "newClass"
print soup.p
del soup.p['class']
print soup.p
print soup.p.string
print type(soup.p.string)
print type(soup.name)
print soup.name
print soup.attrs
print soup.a
print soup.a.string
print type(soup.a.string)

print soup.head.contents
print soup.head.contents[0]

print soup.head.children
for child in soup.head.children:
    print child
